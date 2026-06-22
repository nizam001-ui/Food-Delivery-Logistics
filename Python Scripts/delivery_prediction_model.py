import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

# Assuming 'df' is your loaded DataFrame
# 1. Prepare Data (Convert text categories to numbers for the model)
features = df[['Order_Value', 'Order_Hour', 'Day_Type', 'Weather']]
features = pd.get_dummies(features, drop_first=True) # One-hot encoding

target = df['Delivery_Time_Mins']

# 2. Split Data
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# 3. Train the Demand/Logistics Model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 4. Evaluate
predictions = rf_model.predict(X_test)
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
