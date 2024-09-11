```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
    x (int): The number to be converted.
    base (int): The target base for the conversion.

    Returns:
    str: The string representation of x in the target base.
    """
    convertString = "0123456789"

    # Handle negatives
    if x < 0:
        sign = "-"
        x = -x
    else:
        sign = ""

    # Convert to the target base
    result = ""
    while x:
        x, remainder = divmod(x, base)
        result = convertString[remainder] + result

    # Add the sign
    result = sign + result if result else sign

    return result


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script uses a simple iterative approach to convert the input number `x` to the target base. The `divmod` function is used to get the quotient and remainder of the division of `x` by `base`, and these values are used to build the result string from right to left. The base numbers are represented by the first 10 characters of the string `'0123456789'`.