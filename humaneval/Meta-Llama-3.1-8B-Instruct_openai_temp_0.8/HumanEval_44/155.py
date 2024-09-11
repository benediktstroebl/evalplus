```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
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

    result = ''
    while x > 0:
        result = str(x % base) + result
        x = x // base

    return result

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that converts a given number `x` to a target base `base`. The function uses the standard division and modulus operators to repeatedly divide the input number by the target base and append the remainder to the result string. If the input number is 0, the function returns '0' immediately. The test cases at the end demonstrate the function's usage.