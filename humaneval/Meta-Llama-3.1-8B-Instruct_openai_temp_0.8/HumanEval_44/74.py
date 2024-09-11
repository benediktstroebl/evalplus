```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
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
    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a recursive function `change_base` that converts a number `x` from decimal to another base `base`. If the number `x` is less than the base, it simply converts it to a string. If the number is greater than or equal to the base, it recursively converts the quotient of `x` divided by `base` to the same base and appends the remainder of `x` divided by `base` to the result.