```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The target base for the conversion.
    
    Returns:
    str: String representation of the number in the target base.
    
    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    digits = "0123456789"
    if x < base:
        return digits[x]
    else:
        return change_base(x // base, base) + digits[x % base]


# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a recursive function `change_base` that converts a number `x` to a base `base` by repeatedly dividing `x` by `base` and appending the remainder to the result string. The function uses a string `digits` to map the remainder (0-9) to its corresponding digit. If the remainder is less than the base, it directly returns the corresponding digit. Otherwise, it recursively calls itself with the quotient and appends the corresponding digit to the result string.