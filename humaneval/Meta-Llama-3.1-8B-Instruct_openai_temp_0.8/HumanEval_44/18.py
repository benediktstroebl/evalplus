```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        # Special case for 0
        return '0'

    converted = ''
    while x > 0:
        # Get remainder of x divided by base
        remainder = x % base
        # Prepend remainder to the result
        converted = str(remainder) + converted
        # Update x to be the quotient of x divided by base
        x = x // base

    return converted

# Example usage:
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script uses a while loop to continuously divide the input number `x` by the target base, prepending the remainder to the result string each time. This effectively "reverses" the decimal conversion process, returning the input number in the desired base.