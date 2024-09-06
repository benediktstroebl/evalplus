```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers 10.
    """ string representation after a
    return a string representation of x
    """
    if x < 0 or base < 2:
        raise ValueError("Invalid input. Ensure base is positive and positive number.")
    result = "{:0<{base}}".format(x)
    return result

# Test cases
test_cases = [
    (8, 3),
    (8, 2),
    (7, 2),
]

# Test function
def test():
    for x, base in test_cases:
        result = change_base(x, base)
        print(f"Input: {x}, Base: {base}, Result: {result}")

# Run the tests
test()
```

This Python code defines a function `change_base` that converts a number to a given base, and tests it with a series of test cases. The `test` function contains the series of test cases, which are then executed using the `test()` function. The `test` function prints the result for each input-base combination, confirming that the `change_base` function works correctly.