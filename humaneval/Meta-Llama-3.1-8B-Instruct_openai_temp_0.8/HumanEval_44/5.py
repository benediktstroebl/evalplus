```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Returns the string representation after the conversion.
    Base numbers are less than 10.

    Args:
        x (int): The number to be converted.
        base (int): The base to which the number is to be converted.

    Returns:
        str: The string representation of x in the base specified.

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

    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''

    while x > 0:
        result = digits[x % base] + result
        x //= base

    return result


# Test the function
print(change_base(8, 3))  # Expected output: '22'
print(change_base(8, 2))  # Expected output: '1000'
print(change_base(7, 2))  # Expected output: '111'
```

This script defines a function `change_base` that converts a number `x` from base 10 to any base less than 10. The function uses integer division and modulo operation to extract the digits of the number in the target base, and then converts them to the corresponding characters in the string representation. The script includes documentation and example use cases to demonstrate the function's behavior.