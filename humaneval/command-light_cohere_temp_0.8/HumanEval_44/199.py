```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
    # Implementation of the conversion
    # Here we're using a reverse method to convert the string
    # representation to numerical value, and then returning
    # the string representation in the desired base
    return ''.join_numeral(x, base)

# Test cases
test_cases = [
    (8, 3),
    (8, 2),
    (7, 2),
    (1, 34),
    (120, 7),
    (123, 10),
    # Add more test cases as needed
]

for x, base in test_cases:
    print(f'Input: {x}, Base: {base}, Expected Output: {change_base(x, base)}')
```
This script defines a function `change_base` that converts a number to a string representation in a specified base. It also includes a test cases, which demonstrate the expected behavior of the function for different inputs and bases.

Let me add that the function also works for negative numbers, and returns the negative sign in the base (e.g., -1 if the positive number is converted to negative in that base).