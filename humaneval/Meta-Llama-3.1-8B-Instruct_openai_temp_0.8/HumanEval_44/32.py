```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): Input number
    base (int): Target base
    
    Returns:
    str: String representation of x in base base
    
    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base < 2 or base >= 10:
        raise ValueError("Base must be between 2 and 9")
    
    if x == 0:
        return '0'
    
    digits = "0123456789"
    result = ''
    
    while x:
        x, remainder = divmod(x, base)
        result = digits[remainder] + result
    
    return result

# Test cases
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

This script uses a while loop to repeatedly divide the input number `x` by the target base `base`, appending the remainder to the result string. The remainder is converted to a digit using the `digits` string. The loop continues until `x` becomes 0. The function also includes error checking to ensure that the base is between 2 and 9.