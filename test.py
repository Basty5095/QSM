import openpyxl
from openpyxl.styles import Font, Alignment

# Create a new workbook and select the active worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Add some data to the worksheet
worksheet['A1'] = 'Name'
worksheet['B1'] = 'Age'
worksheet['A2'] = 'John'
worksheet['B2'] = 25
worksheet['A3'] = 'Alice'
worksheet['B3'] = 30

# Add some formatting to the worksheet
bold_font = Font(bold=True)
center_alignment = Alignment(horizontal='center')
worksheet['A1'].font = bold_font
worksheet['B1'].font = bold_font
worksheet['A1'].alignment = center_alignment
worksheet['B1'].alignment = center_alignment

# Save the workbook to a file
workbook.save('example.xlsx')
