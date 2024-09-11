```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The input number to be converted.
    base (int): The target base of the output number.

    Returns:
    str: The string representation of the converted number.

    Example:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    convertString = "0123456789"
    result = ""

    while x > 0:
        # Extract the remainder of x divided by base
        remainder = x % base
        # Prepend the corresponding digit to the result
        result = convertString[remainder] + result
        # Update x to be the quotient of x divided by base
        x = x // base

    return result

# Test the function
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns a string representation of the number `x` in base `base`. The conversion is done by repeatedly taking the remainder of `x` divided by `base` and prepending the corresponding digit to the result. The process is repeated until `x` becomes 0.