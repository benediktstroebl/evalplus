```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Returns string representation after the conversion.
    base numbers are less than 10.

    Args:
        x (int): The number to be converted.
        base (int): The target base.

    Returns:
        str: The string representation of the number in the target base.
    """
    convertString = "0123456789"
    if x < base:
        return convertString[x]
    else:
        return change_base(x // base, base) + convertString[x % base]


# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script uses recursion to convert the base of a number. If the number is less than the target base, it simply returns the string representation of the number. Otherwise, it recursively calls itself with the quotient and remainder of the number divided by the target base, and concatenates the string representation of the remainder to the result.