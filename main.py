import csv

# Data for house prices and square footage
data = [
    {"Price": 250000, "Square footage": 2000},
    {"Price": 350000, "Square footage": 2500},
    {"Price": 450000, "Square footage": 3000},
    {"Price": 550000, "Square footage": 3500},
    {"Price": 650000, "Square footage": 4000}
]

# Write data to CSV file
with open('house-price.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Price', 'Square footage'])
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print("CSV file 'house-price.csv' has been created successfully.")

