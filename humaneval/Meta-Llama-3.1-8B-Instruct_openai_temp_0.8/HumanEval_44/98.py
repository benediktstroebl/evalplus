```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
        x (int): The input number to be converted.
        base (int): The base to which the number should be converted.

    Returns:
        str: The string representation of the number in the new base.

    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'

    digits = '0123456789ABCDEF'
    new_base = ''

    while x:
        new_base = digits[x % base] + new_base
        x //= base

    return new_base


# Test the function
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
print(change_base(10, 2))  # '1010'
print(change_base(15, 16))  # 'F'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input and returns the string representation of `x` in the new base. The function uses a while loop to repeatedly divide `x` by `base` and append the remainder (as a digit in the new base) to the front of the result string.