-- Sales by Region
SELECT
	resion,
	SUM(sales_amount) AS total_sales
FROM sales_data
GROUP BY resion
ORDER BY total_sales DESC;
-- Sales by Category
SELECT
    category,
    SUM(sales_amount) AS total_sales
FROM sales_data
GROUP BY category
ORDER BY total_sales DESC;
-- Sales by Sales Representative
SELECT
    sales_rep,
    SUM(sales_amount) AS total_sales
FROM sales_data
GROUP BY sales_rep
ORDER BY total_sales DESC;
-- Customer and Sales JOIN
SELECT
    s.order_id,
    s.customer_name,
    c.customer_id,
    c.resion,
    s.sales_amount
FROM sales_data AS s
INNER JOIN customers AS c
    ON s.customer_id = c.customer_id
LIMIT 20;
-- Customer Sales Ranking
SELECT
    customer_id,
    customer_name,
    SUM(sales_amount) AS total_sales,
    RANK() OVER (
        ORDER BY SUM(sales_amount) DESC
    ) AS sales_rank
FROM sales_data
GROUP BY customer_id, customer_name
ORDER BY sales_rank;
-- Monthly Sales Trend
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(sales_amount) AS total_sales
FROM sales_data
GROUP BY month
ORDER BY month;
-- Customer Ranking Within Region
SELECT
    resion,
    customer_id,
    customer_name,
    SUM(sales_amount) AS total_sales,
    RANK() OVER (
        PARTITION BY resion
        ORDER BY SUM(sales_amount) DESC
    ) AS region_rank
FROM sales_data
GROUP BY resion, customer_id, customer_name
ORDER BY resion, region_rank;
-- Top 5 Products by Sales
SELECT
    product,
    SUM(sales_amount) AS total_sales
FROM sales_data
GROUP BY product
ORDER BY total_sales DESC
LIMIT 5;
