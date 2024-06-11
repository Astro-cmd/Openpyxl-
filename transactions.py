from openpyxl import Workbook, load_workbook
import numpy as np
import pandas as pd

# Step 1: Generate data using numpy and pandas
np.random.seed(0)
months = pd.date_range(start='2023-01-01', periods=12, freq='M')
sales = np.random.randint(10000, 50000, size=12)
transactions = np.random.randint(50, 200, size=12)

data = {
    'Month': months,
    'Sales': sales,
    'Transactions': transactions
}
df = pd.DataFrame(data)
'''
# Step 2: Save DataFrame to a new Excel file using pandas
df.to_excel('new_transactions.xlsx', index=False)

# Step 3: Load the newly created workbook using openpyxl to add new data
wb = load_workbook('new_transactions.xlsx')
ws = wb.active
ws.title = 'Transactions'

# Save the workbook again with any modifications
wb.save('new_transactions.xlsx')

'''
print(data)