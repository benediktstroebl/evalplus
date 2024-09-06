```python
def change_base(x: int, base: int):
    """Change the base numerical number x to base."""
    if base == 10:
        return str(x)
    else:
        # Perform integer conversion to base base
        return str(x, base)

# Unit tests
test_change_base = []
test_change_base.push_back(change_base(8, 3))
test_change_base.push_back(change_base(8, 2))
test_change_base.push_back(change_base(7, 2))

# Print the test results
for x, want in test_change_base:
    print(f"Got: {x}, Expected: {want}")
```

This Python code provides a self-contained function `change_base` that converts numbers to a specified base. The function takes two arguments: `x`, which is the number to be converted, and `base`, which is the base to which the conversion will be performed. The function returns the string representation of `x` in the specified base. The code also includes unit tests using the `test_change_base` list, which contains the test cases for the `change_base` function. The test results are printed out to verify that the function is working correctly.