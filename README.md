# Financial Analysis & Rule-Based Chatbot | BCG GenAI Job Simulation

## Project Overview

This project was completed as part of the **BCG Generative AI Job Simulation on Forage**. It combines financial data analysis with the development of a rule-based chatbot prototype to answer predefined financial questions.

The project focuses on three publicly traded companies: **Microsoft, Tesla, and Apple**, using financial data from their annual SEC 10-K filings for fiscal years 2023–2025.

## Project Objectives

- Extract and organize financial information from annual SEC filings.
- Analyze financial performance using Python and pandas.
- Calculate year-over-year changes and financial ratios.
- Visualize financial trends and comparisons.
- Develop a rule-based chatbot to retrieve financial information.
- Test and document the chatbot's functionality.

## Technologies Used

- **Python** — Financial calculations and chatbot development
- **pandas** — Data processing, filtering, and analysis
- **Matplotlib** — Financial data visualization
- **Jupyter Notebook** — Interactive financial analysis
- **CSV and Excel** — Financial data storage
- **Visual Studio Code** — Development environment

## Part 1: Financial Data Analysis

Collected and analyzed financial information for Microsoft, Tesla, and Apple across three fiscal years.

The analysis included:

- Total revenue
- Net income
- Total assets
- Total liabilities
- Operating cash flow
- Year-over-year revenue and net income growth
- Net profit margin
- Company-level financial comparisons

Used pandas to organize financial records, calculate performance metrics, and summarize trends.

Created visualizations to compare financial performance across companies and years.

The analysis is available in the `BCG_Financial_Analysis` folder, including the Jupyter Notebook and exported HTML report.

## Part 2: Financial Chatbot Prototype

Developed a Python-based rule-based chatbot that answers five predefined financial questions using the financial dataset.

### Supported Questions

1. What is the total revenue?
2. What is the net income?
3. How has net income changed over the last year?
4. What is the operating cash flow?
5. What is the net profit margin?

The chatbot uses pandas to retrieve financial data and conditional logic to return formatted responses.

### Example Interaction

**Question:** What is the total revenue?

**Company:** Apple

**Year:** 2025

**Response:** Apple's total revenue in 2025 was $416,161 million.

## Project Structure

```text
BCG-GenAI-Financial-Analysis-Chatbot/
|
|-- BCG_Financial_Analysis/
|   |-- Financial_Analysis.ipynb
|   |-- Financial_Analysis.html
|   |-- Financial_Data_2023_2025.csv
|   |-- Financial_Data_2023_2025.xlsx
|
|-- BCG_Chatbot_Prototype/
|   |-- financial_chatbot.py
|   |-- Financial_Data_2023_2025.csv
|   |-- README.md
|   |-- test_results.txt
|
|-- README.md
```

## How to Run the Chatbot

1. Install Python and pandas.
2. Open the `BCG_Chatbot_Prototype` folder.
3. Keep the Python script and CSV dataset in the same folder.
4. Run `python financial_chatbot.py` in the terminal.
5. Enter a supported financial question, company name, and year.

## Testing and Limitations

All five predefined questions were manually tested successfully.

The chatbot supports only Microsoft, Tesla, and Apple for 2023–2025. It does not use an LLM, support unrestricted natural-language conversations, or retrieve live financial data.

## Skills Demonstrated

- Financial data extraction and organization
- Python programming
- Data analysis with pandas
- Financial ratio calculations
- Data visualization
- Rule-based chatbot development
- Testing and technical documentation

## Acknowledgment

Completed independently as part of the **BCG Generative AI Job Simulation hosted on Forage**. This project is a learning simulation and does not represent employment at BCG.
