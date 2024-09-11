```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    
    digits = "0123456789"
    if base < 2 or base >= 10:
        raise ValueError("Base must be between 2 and 9")
    
    result = ""
    while x > 0:
        result = digits[x % base] + result
        x = x // base
    
    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that converts a given integer `x` to a specified base `base`. The base must be between 2 and 9, and the function returns a string representation of the number in the specified base. The script includes test cases to demonstrate the function's behavior.