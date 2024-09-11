```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    base numbers are less than 10.

    Args:
        x (int): The number to be converted.
        base (int): The target base.

    Returns:
        str: The string representation of x in base.
    """
    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script works by recursively dividing the number `x` by the target base, appending the remainder to the result string, until `x` is less than the base. At this point, `x` is converted to a string and prepended to the result string, and the function returns the result.