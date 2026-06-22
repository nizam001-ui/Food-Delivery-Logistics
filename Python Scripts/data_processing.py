import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
rows = 3000

# Setup categories
restaurant_types = ['Fast Food', 'Sushi', 'Italian', 'Healthy/Vegan', 'Indian']
weather_conditions = ['Clear', 'Rain', 'Cloudy', 'Storm']
day_types = ['Weekday', 'Weekend', 'Holiday']

data = []
start_date = datetime(2025, 1, 1)

for i in range(rows):
    # Time and Date logic
    order_time = start_date + timedelta(days=int(np.random.randint(0, 180)), hours=int(np.random.randint(10, 23)))
    day_of_week = order_time.weekday()
    day_type = 'Weekend' if day_of_week >= 5 else 'Weekday'
    
    rest_type = np.random.choice(restaurant_types)
    weather = np.random.choice(weather_conditions, p=[0.6, 0.2, 0.15, 0.05])
    
    # Financials
    order_value = round(np.random.uniform(15.0, 120.0), 2)
    
    # Logistics Logic: Rain/Storms and Weekends increase delivery time
    base_time = np.random.randint(15, 35)
    if weather in ['Rain', 'Storm']:
        base_time += np.random.randint(10, 25)
    if day_type == 'Weekend':
        base_time += np.random.randint(5, 15)
        
    delivery_time_mins = base_time
    
    # Customer Rating Logic: Longer delivery = lower rating
    if delivery_time_mins > 50:
        rating = np.random.choice([1, 2, 3], p=[0.5, 0.3, 0.2])
    else:
        rating = np.random.choice([4, 5], p=[0.4, 0.6])
        
    data.append([
        f"ORD-{100000+i}", order_time.strftime('%Y-%m-%d %H:%M:%S'), 
        day_type, rest_type, weather, order_value, delivery_time_mins, rating
    ])

df = pd.DataFrame(data, columns=[
    'Order_ID', 'Order_Timestamp', 'Day_Type', 'Restaurant_Type', 
    'Weather', 'Order_Value', 'Delivery_Time_Mins', 'Customer_Rating'
])

df.to_csv('food_delivery_logistics.csv', index=False)
print("Dataset 'food_delivery_logistics.csv' successfully created with 3,000 rows!")


///////////////////////////////

# import pandas as pd

# # 1. Load Data
# df = pd.read_csv('food_delivery_logistics.csv')

# # 2. Convert Timestamp to actual datetime objects
# df['Order_Timestamp'] = pd.to_datetime(df['Order_Timestamp'])

# # 3. Feature Engineering: Extract the hour to see peak demand times
# df['Order_Hour'] = df['Order_Timestamp'].dt.hour

# # 4. Save the cleaned version for SQL injection
# df.to_csv('cleaned_food_delivery.csv', index=False)