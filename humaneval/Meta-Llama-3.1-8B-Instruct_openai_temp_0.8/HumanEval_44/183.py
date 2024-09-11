```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
        x (int): The number to be converted.
        base (int): The target numerical base.

    Returns:
        str: The string representation of x in the target base.
    """
    if x < base:
        return str(x)

    result = ''
    while x:
        x, remainder = divmod(x, base)
        result = str(remainder) + result

    return result

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script uses a simple iterative approach to perform the base conversion. The `divmod` function is used to get both the quotient and remainder of the division, which is then used to construct the result string from right to left. The function works for bases less than 10 and handles the case where the input number is less than the target base.