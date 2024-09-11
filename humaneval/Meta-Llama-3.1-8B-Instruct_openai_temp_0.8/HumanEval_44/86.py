```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
        x (int): The number to be converted.
        base (int): The target base.

    Returns:
        str: The string representation of x in base base.

    Examples:
        >>> change_base(8, 3)
        '22'
        >>> change_base(8, 2)
        '1000'
        >>> change_base(7, 2)
        '111'
    """
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if x < base:
        return digits[x]
    else:
        return change_base(x // base, base) + digits[x % base]

# Test the function
print(change_base(8, 3))  # Outputs: 22
print(change_base(8, 2))  # Outputs: 1000
print(change_base(7, 2))  # Outputs: 111
```

This script defines a recursive function `change_base` that converts a number `x` from base 10 to a target base. The function uses a string of digits to map the result of the modulo operation to the corresponding digit in the target base. If the number is less than the target base, it returns the corresponding digit directly. Otherwise, it recursively converts the quotient and appends the corresponding digit for the remainder.