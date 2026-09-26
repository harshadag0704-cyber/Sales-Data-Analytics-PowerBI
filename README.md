## sales Data Analytics & Power BI Dashboard
This Project analyzes sales data using Excel,Power Query ,Python ,PostgreSQL,and  Power BI to indentify data sales trends,costomer insights,product performance ,and regional performance.
## Tools & Technologies 
-excel
-power Query
-python (pandas)
-SQL
-Power BI
-DAX
## Data Cleaning

- Inspected missing values and duplicate records using Python Pandas.
- Standardized inconsistent region names.
- Cleaned and validated data using Excel Power Query.
- Corrected data types for dates, quantities, prices, discounts, and sales amounts.
- Exported the cleaned dataset as CSV for SQL and Power BI analysis.
## SQL Analysis

- Created and analyzed sales tables in PostgreSQL.
- Used aggregate functions such as SUM and COUNT.
- Performed GROUP BY and ORDER BY analysis for regions, categories, and sales representatives.
- Used JOINs to combine sales and customer information.
- Applied window functions such as RANK() for customer and regional analysis.
- Analyzed monthly sales trends using date functions.
## Power BI Dashboard

- Built an interactive sales dashboard using Power BI.
- Created KPI cards for Total Sales, Total Orders, Total Customers, and Average Order Value.
- Created Sales by Category and Sales by Region visualizations.
- Created a Monthly Sales Trend chart.
- Added a Top 5 Products by Sales table.
- Added a Date slicer for interactive time-based filtering.
- Created DAX measures for sales, orders, customers, average order value, previous-year sales, and sales growth.
## Key DAX Measures

- Total Sales = SUM of SalesAmount
- Total Orders = DISTINCTCOUNT of OrderID
- Total Customers = DISTINCTCOUNT of CustomerID
- Average Order Value = Total Sales / Total Orders
- Sales LY = Previous-year sales using SAMEPERIODLASTYEAR
- Sales Growth % = Year-over-year sales growth
## Project Outcome

The project provides an interactive view of sales performance across customers, products, categories, regions, sales representatives, and time periods. The Power BI dashboard enables users to filter and explore sales data for business analysis.
## Project Structure

Sales_Data_Analyst/
├── powerbi/
├── python/
├── raw_data1/
├── sql/
└── README.md
## Skills Demonstrated

- Data Cleaning
- Data Transformation
- Exploratory Data Analysis
- SQL Joins & Aggregations
- Window Functions
- Power BI Dashboard Development
- DAX & Time Intelligence
- Business Data Analysis
## Author
 sales data Analytics Project
