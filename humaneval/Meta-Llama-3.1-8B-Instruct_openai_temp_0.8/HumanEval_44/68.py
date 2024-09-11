```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Parameters:
    x (int): The number to be converted.
    base (int): The target base.

    Returns:
    str: The string representation of the number in the target base.

    Example:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'

    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    while x > 0:
        result = digits[x % base] + result
        x //= base

    return result


# Test cases
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in the target base. It uses the standard method of converting a decimal number to another base by repeatedly dividing by the base and appending the remainder to the result. The string representation of the number is then returned. The script also includes test cases to demonstrate the function's behavior.