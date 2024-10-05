# Ask user for their name and remove extra whitespace
name = input("What's your name? ").strip().title()

# Greet the user with their capitalized name
print(f"Hello, {name}")

# INSIGHTS:
# 1. Input Handling:
#    - input() asks the user to enter their name.
#    - strip() removes any leading or trailing whitespace.
#    - title() capitalizes the first letter of each word (e.g., first and last names).
#
# 2. Name Splitting (Optional):
#    - If you want to separate first and last names for more processing, you can use:
#        first, last = name.split()
#    - This assumes the user enters both first and last names.
#    - Example: "John Doe" will be split into first = "John" and last = "Doe".
#
# 3. String Manipulation:
#    - strip() is used to remove whitespace before and after the string.
#    - title() is used to capitalize the first letter of each word.
#
# 4. Multiple Ways to Print:
#    - print(f'Hello, {name}') is the most efficient way to format strings using f-strings.
#    - Other approaches include:
#        - print('hello,', name)
#        - print('Hello, ' + name) (concatenation)
#    - print('Hello, ', end='') allows you to control the end character (default is '\n', a newline).
#    - print('Hello, ', name, sep='') controls the separator (default is space ' ').
#
# 5. Best Practices:
#    - Using strip() ensures no extra spaces are accidentally included in the name.
#    - Using title() ensures proper capitalization for names with multiple words.
#    - It's good practice to keep code concise and avoid redundant operations,
#       such as calling strip() or title() multiple times.
