```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
    x (int): The number to be converted.
    base (int): The base to convert to.

    Returns:
    str: The string representation of x in base.

    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'

    digits = []
    while x:
        digits.append(int(x % base))
        x //= base

    return ''.join(map(str, digits[::-1]))


# Example usage
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines the `change_base` function to convert an integer `x` to a given base. It uses a while loop to repeatedly divide `x` by the base and append the remainder to the list of digits. The digits are then reversed and joined together into a string, with each digit represented as a string. The result is the string representation of `x` in the given base.