Query 1 - Total Sales
SELECT ROUND(SUM(Sales),2) AS Total_Sales
FROM samplesuperstore;

Query 2 - Total Profit
SELECT ROUND(SUM(Profit),2) AS Total_Profit
FROM samplesuperstore;

Query 3 - Total Orders
SELECT COUNT(*) AS Total_Orders
FROM samplesuperstore;

Query 4 - Region Analysis
SELECT Region,
ROUND(SUM(Sales),2) AS Total_Sales,
ROUND(SUM(Profit),2) AS Total_Profit
FROM samplesuperstore
GROUP BY Region
ORDER BY Total_Sales DESC;

Query 5 - Top States by Sales
SELECT State,
ROUND(SUM(Sales),2) AS Total_Sales
FROM samplesuperstore
GROUP BY State
ORDER BY Total_Sales DESC
LIMIT 10;

Query 6 - Top States by Profit
SELECT State,
ROUND(SUM(Profit),2) AS Total_Profit
FROM samplesuperstore
GROUP BY State
ORDER BY Total_Profit DESC
LIMIT 10;

Query 7 - Category Wise Sales
SELECT Category,
ROUND(SUM(Sales),2) AS Total_Sales
FROM samplesuperstore
GROUP BY Category
ORDER BY Total_Sales DESC;

Query 8 - Category Wise Profit
SELECT Category,
ROUND(SUM(Profit),2) AS Total_Profit
FROM samplesuperstore
GROUP BY Category
ORDER BY Total_Profit DESC;

Query 9 - Top Cities by Sales
SELECT City,
ROUND(SUM(Sales),2) AS Total_Sales
FROM samplesuperstore
GROUP BY City
ORDER BY Total_Sales DESC
LIMIT 10;

Query 10 - Loss Making Sub-Categories
SELECT `Sub-Category`,
ROUND(SUM(Profit),2) AS Total_Profit
FROM samplesuperstore
GROUP BY `Sub-Category`
ORDER BY Total_Profit ASC
LIMIT 10;