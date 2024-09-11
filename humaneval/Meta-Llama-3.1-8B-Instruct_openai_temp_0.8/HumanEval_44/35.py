```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Args:
        x (int): The number to be converted.
        base (int): The base to convert to.
    
    Returns:
        str: The string representation of x in base.
    """
    if not 2 <= base <= 9:
        raise ValueError("Base must be between 2 and 9")
    
    if x == 0:
        return '0'
    
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    
    while x:
        result = digits[x % base] + result
        x //= base
    
    return result

# Test cases
print(change_base(8, 3))  # Should print: '22'
print(change_base(8, 2))  # Should print: '1000'
print(change_base(7, 2))  # Should print: '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `b` as input and returns a string representation of `x` in base `b`. The function uses the digits 0-9 and A-Z to represent the digits in the new base. If the base is less than 2 or greater than 9, it raises a ValueError.