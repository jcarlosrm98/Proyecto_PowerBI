import pandas as pd
import numpy as np
import uuid
from datetime import datetime, timedelta

# Utility function to generate random dates
def random_date(start, end):
    return start + timedelta(seconds=np.random.randint(0, int((end - start).total_seconds())))

# Define the number of data points
num_records = 100000

# Customers Table
# Contains customer information
customers = pd.DataFrame({
    'Customer_ID': [str(uuid.uuid4()) for _ in range(num_records)],
    'Customer_Name': [f"Customer_{i}" for i in range(num_records)],
    'Address': [f"Address_{i}" for i in range(num_records)],
    'City': [f"City_{np.random.randint(1, 50)}" for _ in range(num_records)],
    'State': [f"State_{np.random.randint(1, 50)}" for _ in range(num_records)],
    'Postal_Code': [f"{np.random.randint(10000, 99999)}" for _ in range(num_records)],
    'Phone_Number': [f"{np.random.randint(10000000, 99999999)}" for _ in range(num_records)]
})

# Suppliers Table
# Contains supplier information
suppliers = pd.DataFrame({
    'Supplier_ID': [str(uuid.uuid4()) for _ in range(num_records)],
    'Supplier_Name': [f"Supplier_{i}" for i in range(num_records)],
    'Address': [f"Address_{i}" for i in range(num_records)],
    'City': [f"City_{np.random.randint(1, 50)}" for _ in range(num_records)],
    'State': [f"State_{np.random.randint(1, 50)}" for _ in range(num_records)],
    'Postal_Code': [f"{np.random.randint(10000, 99999)}" for _ in range(num_records)],
    'Phone_Number': [f"{np.random.randint(10000000, 99999999)}" for _ in range(num_records)]
})

# Products Table
# Contains product information (Gasoline types, etc.)
products = pd.DataFrame({
    'Product_ID': [str(uuid.uuid4()) for _ in range(50)],
    'Product_Name': [f"Product_{i}" for i in range(50)],
    'Product_Description': [f"Description_{i}" for i in range(50)],
    'Unit_Price': [round(np.random.uniform(10, 100), 2) for _ in range(50)]
})

# Orders Table
# Contains order information (which customer ordered which product)
orders = pd.DataFrame({
    'Order_ID': [str(uuid.uuid4()) for _ in range(num_records)],
    'Customer_ID': [np.random.choice(customers['Customer_ID']) for _ in range(num_records)],
    'Order_Date': [random_date(datetime(2020, 1, 1), datetime(2024, 12, 31)) for _ in range(num_records)],
    'Product_ID': [np.random.choice(products['Product_ID']) for _ in range(num_records)],
    'Quantity': [np.random.randint(1, 100) for _ in range(num_records)],
    'Total_Amount': [round(np.random.uniform(100, 1000), 2) for _ in range(num_records)]
})

# Inventory Table
# Contains inventory information (how much of each product is in stock)
inventory = pd.DataFrame({
    'Inventory_ID': [str(uuid.uuid4()) for _ in range(num_records)],
    'Product_ID': [np.random.choice(products['Product_ID']) for _ in range(num_records)],
    'Quantity_Available': [np.random.randint(100, 10000) for _ in range(num_records)],
    'Last_Updated': [random_date(datetime(2020, 1, 1), datetime(2024, 12, 31)) for _ in range(num_records)]
})

# Shipments Table
# Contains shipment information (which supplier shipped which product)
shipments = pd.DataFrame({
    'Shipment_ID': [str(uuid.uuid4()) for _ in range(num_records)],
    'Supplier_ID': [np.random.choice(suppliers['Supplier_ID']) for _ in range(num_records)],
    'Product_ID': [np.random.choice(products['Product_ID']) for _ in range(num_records)],
    'Shipment_Date': [random_date(datetime(2020, 1, 1), datetime(2024, 12, 31)) for _ in range(num_records)],
    'Quantity_Shipped': [np.random.randint(100, 10000) for _ in range(num_records)]
})

# Employees Table
# Contains employee information (who works at the company)
employees = pd.DataFrame({
    'Employee_ID': [str(uuid.uuid4()) for _ in range(1000)],
    'Employee_Name': [f"Employee_{i}" for i in range(1000)],
    'Position': [f"Position_{np.random.randint(1, 10)}" for _ in range(1000)],
    'Salary': [round(np.random.uniform(30000, 150000), 2) for _ in range(1000)],
    'Hire_Date': [random_date(datetime(2015, 1, 1), datetime(2024, 12, 31)) for _ in range(1000)]
})

# Departments Table
# Contains department information (which departments exist in the company)
departments = pd.DataFrame({
    'Department_ID': [str(uuid.uuid4()) for _ in range(10)],
    'Department_Name': [f"Department_{i}" for i in range(10)],
    'Manager_ID': [np.random.choice(employees['Employee_ID']) for _ in range(10)]
})

# Employee-Department Relationships
# Defines which employees belong to which departments
employee_department = pd.DataFrame({
    'Employee_ID': [np.random.choice(employees['Employee_ID']) for _ in range(num_records)],
    'Department_ID': [np.random.choice(departments['Department_ID']) for _ in range(num_records)],
    'Start_Date': [random_date(datetime(2015, 1, 1), datetime(2024, 12, 31)) for _ in range(num_records)]
})

# Revenue Table
# Contains revenue information (monthly revenue of the company)
revenue = pd.DataFrame({
    'Revenue_ID': [str(uuid.uuid4()) for _ in range(60)],
    'Month_Year': [f"{month}/{year}" for year in range(2020, 2025) for month in range(1, 13)],
    'Total_Revenue': [round(np.random.uniform(100000, 1000000), 2) for _ in range(60)]
})

# Save all dataframes to CSV
customers.to_csv('customers.csv', index=False)
suppliers.to_csv('suppliers.csv', index=False)
products.to_csv('products.csv', index=False)
orders.to_csv('orders.csv', index=False)
inventory.to_csv('inventory.csv', index=False)
shipments.to_csv('shipments.csv', index=False)
employees.to_csv('employees.csv', index=False)
departments.to_csv('departments.csv', index=False)
employee_department.to_csv('employee_department.csv', index=False)
revenue.to_csv('revenue.csv', index=False)

print("Synthetic data model created and exported to CSV files.")
