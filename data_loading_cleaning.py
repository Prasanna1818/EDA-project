#Task 1
#Exploratory Data Analysis (EDA) on Retail Sales Data

import matplotlib
matplotlib.use('TkAgg')  # Use Tkinter backend
import pandas as pd
import matplotlib.pyplot as plt

# Load the retail sales dataset
retail_data = pd.read_csv(r"E:\project-1\retail_sales_dataset.csv")

# Display the first few rows of the dataset to understand its structure
print(retail_data.head())

# Check for missing values, duplicates, and inconsistencies in the dataset
print("\nMissing Values:")
print(retail_data.isnull().sum())
print("\nDuplicates:")
print(retail_data.duplicated().sum())

# Handle missing or inconsistent data
retail_data.dropna(inplace=True)
retail_data.drop_duplicates(inplace=True)

# Display the cleaned dataset
print("\nCleaned Dataset:")
print(retail_data.head())

# Calculate descriptive statistics
descriptive_stats = retail_data.describe()

# Calculate mode
mode = retail_data.mode()

# Display descriptive statistics and mode
print("\nDescriptive Statistics:")
print(descriptive_stats)
print("\nMode:")
print(mode)

# Convert 'Date' column to datetime format
retail_data['Date'] = pd.to_datetime(retail_data['Date'])

# Set 'Date' column as the index
retail_data.set_index('Date', inplace=True)

# Resample data to monthly frequency and calculate total sales
monthly_sales = retail_data.resample('M').sum()

# Plot monthly sales trends
plt.plot(monthly_sales.index, monthly_sales['Total Amount'])
plt.xlabel('Date')
plt.ylabel('Total Sales Amount')
plt.title('Monthly Sales Trends')
plt.show()

# Customer demographics analysis
customer_demographics = retail_data.groupby('Gender').agg({'Age': 'mean', 'Total Amount': 'sum'})

# Plotting customer demographics
plt.figure(figsize=(8, 6))
plt.bar(customer_demographics.index, customer_demographics['Total Amount'], color=['blue', 'orange'])
plt.xlabel('Gender')
plt.ylabel('Total Sales Amount')
plt.title('Total Sales Amount by Gender')
plt.xticks(rotation=45)  
plt.show()

# Product performance analysis
product_performance = retail_data.groupby('Product Category').agg({'Quantity': 'sum', 'Total Amount': 'sum'})
print("\nCustomer Demographics:")
print(customer_demographics)
print("\nProduct Performance:")
print(product_performance)
