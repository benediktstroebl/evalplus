```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): the number to convert
    base (int): the base to convert to (less than 10)
    
    Returns:
    str: the string representation of the converted number
    
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
    
    result = ''
    while x > 0:
        x, remainder = divmod(x, base)
        result = str(remainder) + result
    
    return result

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This Python script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns a string representation of `x` in the given base. The function uses a while loop to repeatedly divide `x` by `base` and prepend the remainder to the result string. The function handles the case where `x` is 0 by immediately returning '0'.