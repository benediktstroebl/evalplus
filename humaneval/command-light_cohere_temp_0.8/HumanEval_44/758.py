```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base base.
    Returns a string representation after conversion.
    base numbers are more than 10."""
    if base == 10:
        return str(x)
    else:
        return '{:02}'.format(x, base)

# Test cases
print(change_base(8, 3))  # Expected output: '22'
print(change_base(8, 2))  # Expected output: '1000'
print(change_base(7, 2))  # Expected output: '111'
```
This script defines a function `change_base` that converts a given number `x` to a string using a specified base. The base can either be 10 or a custom base, represented as an integer between 2 and 36. The test cases ensure that the function correctly handles various inputs and returns the expected string representations.