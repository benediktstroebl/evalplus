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
    """
    convertString = "0123456789ABCDEF"
    if x < base:
        return convertString[x]
    else:
        return change_base(x // base, base) + convertString[x % base]


# Test the function
print(change_base(8, 3))   # Output: '22'
print(change_base(8, 2))   # Output: '1000'
print(change_base(7, 2))   # Output: '111'
```
This script uses recursion to convert the number to the target base. It handles the case where `x` is less than `base` by directly looking up the string representation of `x` in the `convertString` dictionary. Otherwise, it calculates the quotient and remainder of `x` divided by `base` and recursively converts the quotient to the target base, then appends the string representation of the remainder.