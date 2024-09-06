Here is a Python script that contains a self-contained function that sorts and returns a list of numbers in ascending order:
```python
# Function to sort list of numbers in ascending order
def sort_numbers(numbers: str) -> str:
    # Convert string to list of numbers
    numbers = list(map(float, numbers. Such that: numbers! use the list comprehension to split the string into a list of numbers and map them to float. Then, sort the list using the sorted() function to sort the numbers in ascending order.

# Test cases
test_cases = {
#   "two three four five six seven eight nine": "two three four five six seven eight nine",
#   "zero one two three four five six seven eight nine": "two three four five six seven eight nine",
#   "five six seven eight nine": "five six seven eight nine",
#   "zero": "zero",
#   "one two three four five six seven eight nine":"one two three four five six seven eight nine",
# }

for test_case, expected in test_cases:
    # Call the function with test_case string as input
    actual = sort_numbers(test_case)
    # Print actual and expected values
    print(f"Test case '{test_case}': actual: {actual}, expected: {expected}")
```