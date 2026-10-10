# BCG Financial Chatbot Prototype

## Project Overview

This project is a rule-based financial chatbot prototype developed using Python and pandas as part of the BCG Forage simulation.

The chatbot responds to five predefined financial questions using historical financial data from Apple, Microsoft, and Tesla for fiscal years 2023–2025.

## Tools and Technologies

- Python
- pandas
- CSV dataset
- Visual Studio Code

## How the Chatbot Works

1. The chatbot loads financial data from `Financial_Data_2023_2025.csv` using pandas.
2. The user enters a financial question, company name, and year.
3. The chatbot uses `if-elif-else` statements to identify the predefined question.
4. It retrieves the relevant financial data from the dataset.
5. It returns a formatted response containing the requested financial information.

## Supported Financial Queries

1. What is the total revenue?
2. What is the net income?
3. How has net income changed over the last year?
4. What is the operating cash flow?
5. What is the net profit margin?

## Testing

The chatbot was manually tested using all five predefined financial questions. Each test returned the expected financial result.

Additional validation was implemented to handle missing company-year records, invalid years, and unsupported questions.

## Limitations

- The chatbot only supports five predefined financial questions.
- It only contains financial data for Apple, Microsoft, and Tesla from 2023 to 2025.
- Year-over-year net income changes cannot be calculated for 2023 because 2022 data is unavailable.
- The chatbot uses predefined rules rather than artificial intelligence or natural language processing.
- It does not retrieve live financial information.
- It processes one question per execution.

## How to Run

1. Install Python and pandas.
2. Keep `financial_chatbot.py` and `Financial_Data_2023_2025.csv` in the same folder.
3. Open the folder in Visual Studio Code.
4. Run `financial_chatbot.py`.
5. Enter one of the supported questions, a company name, and a year when prompted.

## Conclusion

The prototype demonstrates how Python, pandas, and conditional statements can be combined to create a basic financial question-answering system. It provides a foundation for developing more advanced financial chatbot applications.