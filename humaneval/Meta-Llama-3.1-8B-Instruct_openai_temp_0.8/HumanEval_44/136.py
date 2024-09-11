```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Returns string representation after the conversion.
    Base numbers are less than 10.
    """
    if x == 0:
        return '0'

    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while x > 0:
        x, remainder = divmod(x, base)
        result = digits[remainder] + result
    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in the given base. It uses the `divmod` function to perform integer division and calculate the remainder, then uses a while loop to repeatedly divide the input number by the base and append the corresponding digit to the result string. If the input number is 0, it directly returns '0'.