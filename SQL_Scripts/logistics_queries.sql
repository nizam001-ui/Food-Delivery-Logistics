--Query 1: How does weather impact our delivery SLAs (Service Level Agreements)?
SELECT 
    Weather,
    COUNT(Order_ID) AS Total_Orders,
    ROUND(AVG(Delivery_Time_Mins), 1) AS Avg_Delivery_Time,
    ROUND(AVG(Customer_Rating), 2) AS Avg_Rating
FROM cleaned_food_delivery
GROUP BY Weather
ORDER BY Avg_Delivery_Time DESC;

---

--Which restaurant types drive the most revenue on Weekends?
SELECT 
    Restaurant_Type,
    SUM(Order_Value) AS Total_Revenue
FROM cleaned_food_delivery
WHERE Day_Type = 'Weekend'
GROUP BY Restaurant_Type
ORDER BY Total_Revenue DESC;
