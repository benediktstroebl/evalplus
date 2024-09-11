```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
    x (int): The number to be converted.
    base (int): The target numerical base, less than 10.

    Returns:
    str: The string representation of the number x in the target base.

    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("x and base must be integers")
    if base < 2 or base > 9:
        raise ValueError("base must be between 2 and 9 (inclusive)")
    if x < 0:
        sign = '-'
        x = -x
    else:
        sign = ''

    converted = ''
    while x:
        x, remainder = divmod(x, base)
        converted = str(remainder) + converted

    return sign + converted


# Example usage:
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes an integer `x` and its target base as input, performs the base conversion, and returns the result as a string. The function first checks if the inputs are valid (both integers and within the allowed range for the base). It then performs the conversion by repeatedly dividing the number by the base and prepending the remainder to the result string.