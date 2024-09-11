```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Args:
        x (int): Input number to be converted.
        base (int): Target numerical base.
        
    Returns:
        str: String representation of the converted number.
    
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
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    # reverse the list since we were prepending the digits
    digits.reverse()
    
    return ''.join(map(str, digits))

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, converts `x` to the specified base, and returns the result as a string. It uses a while loop to repeatedly divide `x` by `base` and prepend the remainder to a list of digits. The list is then reversed and joined to form the final string representation. The script includes example test cases at the end.