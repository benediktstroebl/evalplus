### Numerical Base Conversion
```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Parameters:
    x (int): The number to be converted.
    base (int): The base to convert to.

    Returns:
    str: The string representation of x in base.

    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    digits = ''
    while x > 0:
        digits = str(x % base) + digits
        x //= base
    return digits

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This Python script defines a function `change_base` that converts a given integer `x` to a desired base `base`. The function uses a while loop to repeatedly divide the input number by the base and append the remainder to the result string. The result string is then returned. The script also includes example usage and test cases to demonstrate the function's correctness.