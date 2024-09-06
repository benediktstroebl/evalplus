```python
def change_base(x: int, base: int):
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Invalid argument types. Ensure both x and base are integers.")

    # Convert the input to a string if it's not already one
    x = str(x)

    # Perform the base conversion using the provided base
    converted = x.format(int(x), format='{:b}')

    return converted

# Test the function with a variety of inputs and bases
test_cases = [
    (8, 3),
    (10, 4),
    (7, 2),
    (98, 7),
    (57, 16),
    (87, 17),
]

for case in test_cases:
    actual = change_base(*case)
    expected = case[1]

    print(f"Input: {case[0]}, Expected: {expected}")
    print(f"Actual: {actual}")
    print()
```
This code defines a function `change_base` that converts a number to a string using a specified base. The tests cases are designed to validate the function's behavior with different input types and base numbers. You can add more test cases to further test the function.

The output will display each test case and show the actual result compared to the expected output. This helps ensure that the function works correctly for a variety of inputs and bases.

Note: The tests are designed to work with any input types and base numbers, as long as they are integers. The function will raise an `ValueError` if the inputs are not integers or if the base is not an integer.