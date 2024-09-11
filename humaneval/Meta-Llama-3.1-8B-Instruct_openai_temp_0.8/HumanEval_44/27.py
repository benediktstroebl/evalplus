```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
        x (int): The number to be converted.
        base (int): The base to convert to.

    Returns:
        str: The string representation of the number in the new base.
    """
    # Define a string of digits to use for conversion
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if x < base:
        # If the number is less than the base, return the corresponding digit
        return digits[x]
    else:
        # Otherwise, recursively convert the number divided by the base
        return change_base(x // base, base) + digits[x % base]


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script uses a recursive approach to convert the number `x` to the desired base. It uses a string of digits to map the remainder of the division to the corresponding digit in the new base. The function works by recursively dividing the number by the base and prepending the corresponding digit for the remainder to the result.