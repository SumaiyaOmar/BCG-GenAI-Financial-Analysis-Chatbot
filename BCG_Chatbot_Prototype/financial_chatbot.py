
import pandas as pd
from pathlib import Path

# Load the financial dataset from the same folder as this script
file_path = Path(__file__).resolve().parent / "Financial_Data_2023_2025.csv"

df = pd.read_csv(file_path)

# Clean the dataset for consistent matching
df.columns = df.columns.str.strip()
df["Company"] = df["Company"].astype(str).str.strip()
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

financial_columns = [
    "Total Revenue",
    "Net Income",
    "Operating Cash Flow"
]

for column in financial_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")


def simple_chatbot(user_query, company, year):

    # Standardize user input
    question = " ".join(user_query.strip().lower().split())
    company = company.strip().lower()

    # Match company and year
    company_data = df[
        (df["Company"].str.lower() == company) &
        (df["Year"] == year)
    ]

    # First question: Total Revenue
    if question == "what is the total revenue?":

        if company_data.empty:
            return "Sorry, financial data is not available for that company and year."

        revenue = company_data.iloc[0]["Total Revenue"]

        if pd.isna(revenue):
            return "Sorry, revenue data is missing."

        return (
            f"{company.title()}'s total revenue in {year} "
            f"was ${revenue:,.0f} million."
        )

    # Second question: Net Income
    elif question == "what is the net income?":

        if company_data.empty:
            return "Sorry, financial data is not available for that company and year."

        net_income = company_data.iloc[0]["Net Income"]

        if pd.isna(net_income):
            return "Sorry, net income data is missing."

        return (
            f"{company.title()}'s net income in {year} "
            f"was ${net_income:,.0f} million."
        )

    # Third question: Year-over-Year Net Income Change
    elif question in [
        "how has net income changed over the last year?",
        "how has the net income changed over the last year?"
    ]:

        previous_data = df[
            (df["Company"].str.lower() == company) &
            (df["Year"] == year - 1)
        ]

        if company_data.empty or previous_data.empty:
            return "Sorry, net income data is not available for both years."

        current_income = company_data.iloc[0]["Net Income"]
        previous_income = previous_data.iloc[0]["Net Income"]

        if pd.isna(current_income) or pd.isna(previous_income):
            return "Sorry, net income data is missing."

        change = current_income - previous_income

        if change > 0:
            trend = "increased"
        elif change < 0:
            trend = "decreased"
        else:
            trend = "remained unchanged"

        if previous_income == 0:
            return (
                f"{company.title()}'s net income {trend} by "
                f"${abs(change):,.0f} million from {year - 1} to {year}. "
                "Percentage change is undefined because the previous year's "
                "net income was zero."
            )

        percentage_change = (change / abs(previous_income)) * 100

        return (
            f"{company.title()}'s net income {trend} by "
            f"${abs(change):,.0f} million "
            f"({abs(percentage_change):.2f}%) "
            f"from {year - 1} to {year}."
        )

    # Fourth question: Operating Cash Flow
    elif question == "what is the operating cash flow?":

        if company_data.empty:
            return "Sorry, financial data is not available for that company and year."

        cash_flow = company_data.iloc[0]["Operating Cash Flow"]

        if pd.isna(cash_flow):
            return "Sorry, operating cash flow data is missing."

        return (
            f"{company.title()}'s operating cash flow in {year} "
            f"was ${cash_flow:,.0f} million."
        )

    # Fifth question: Net Profit Margin
    elif question == "what is the net profit margin?":

        if company_data.empty:
            return "Sorry, financial data is not available for that company and year."

        revenue = company_data.iloc[0]["Total Revenue"]
        net_income = company_data.iloc[0]["Net Income"]

        if pd.isna(revenue) or pd.isna(net_income):
            return "Sorry, the financial data needed is missing."

        if revenue == 0:
            return "Net profit margin cannot be calculated because revenue is zero."

        profit_margin = (net_income / revenue) * 100

        return (
            f"{company.title()}'s net profit margin in {year} "
            f"was {profit_margin:.2f}%."
        )

    # Unsupported question
    else:
        return "Sorry, I can only answer predefined financial questions."


# Main chatbot interaction
print("Welcome to the BCG Financial Chatbot!")
print("Available companies: Apple, Microsoft, Tesla")
print("Available years: 2023, 2024, 2025")

print("\nAvailable questions:")
print("1. What is the total revenue?")
print("2. What is the net income?")
print("3. How has net income changed over the last year?")
print("4. What is the operating cash flow?")
print("5. What is the net profit margin?")

question = input("\nEnter your financial question: ")
company = input("Enter company (Apple, Microsoft, Tesla): ")

try:
    year = int(input("Enter year (2023, 2024, 2025): "))

    if year not in [2023, 2024, 2025]:
        print("\nChatbot: Please enter a year between 2023 and 2025.")
    else:
        answer = simple_chatbot(question, company, year)
        print("\nChatbot:", answer)

except ValueError:
    print("\nChatbot: Invalid year. Please enter a number such as 2025.")
