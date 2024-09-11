```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
    x (int): The number to be converted.
    base (int): The target base.

    Returns:
    str: The string representation of the number in the target base.

    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    
    digits = '0123456789'
    result = ''
    
    while x > 0:
        x, remainder = divmod(x, base)
        result = digits[remainder] + result
    
    return result

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This Python script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in the target base. The function uses the `divmod` function to perform integer division and find the remainder, and then constructs the result string by prepending the remainder digit to the result. The function also handles the case where `x` is 0. The script includes docstrings and test cases to demonstrate the function's usage.