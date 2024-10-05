# Get two integer inputs from the user
x = int(input("What's x? "))
y = int(input("What's y? "))

# Print the sum of the two integers
print(f'Sum: {x + y}')

# Get two floating-point inputs from the user
x1 = float(input("What's x1? "))
y1 = float(input("What's y1? "))

# Calculate and round the sum of the floating-point numbers
z = round(x1 + y1)
print(f'Rounded sum: {z}')
print(f'Formatted sum with commas: {z:,}')  # Add commas for large numbers

# Get two integer inputs for division
x = int(input("What's x? "))
y = int(input("What's y? "))

# Handle division and round to two decimal places
if y != 0:
    z1 = x / y
    print(f'Rounded division result: {round(z1, 2)}')
    print(f'Formatted division result (2 decimal places): {z1:.2f}')
else:
    print('Error: Division by zero is not allowed.')
