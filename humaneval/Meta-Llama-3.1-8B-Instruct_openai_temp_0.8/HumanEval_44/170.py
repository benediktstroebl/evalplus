```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
        x (int): Number to convert.
        base (int): Base to convert to.

    Returns:
        str: String representation of x in base.

    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    digits = "0123456789"
    result = ""
    while x > 0:
        x, remainder = divmod(x, base)
        result = digits[remainder] + result
    return result


# Test the function
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```
This script defines a function `change_base` that takes an integer `x` and a base `base` as input and returns a string representation of `x` in the given base. The function uses the `divmod` function to get the quotient and remainder of `x` divided by `base`, and then appends the corresponding digit to the result string. The process is repeated until `x` becomes 0. The script also includes test cases to demonstrate the function's correctness.