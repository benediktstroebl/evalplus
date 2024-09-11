```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
        x (int): The number to convert.
        base (int): The base to convert to.

    Returns:
        str: The string representation of the number in the new base.

    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x < base:
        return str(x)

    result = ''
    while x > 0:
        result = str(x % base) + result
        x //= base

    return result

# Test the function
print(change_base(8, 3))  # 22
print(change_base(8, 2))  # 1000
print(change_base(7, 2))  # 111
```

This script defines a function `change_base` that converts an integer `x` to a new base, which must be less than 10. It uses a while loop to repeatedly divide the input number by the base and append the remainder to the result string. If the input number is less than the base, it simply converts it to a string and returns it.