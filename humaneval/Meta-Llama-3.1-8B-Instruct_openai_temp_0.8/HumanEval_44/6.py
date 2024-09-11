```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
        x (int): The number to be converted.
        base (int): The base to convert to.
        
    Returns:
        str: The string representation of x in base base.
    """
    if x == 0:
        return '0'
    
    digits = "0123456789"
    result = ''
    
    while x:
        result = digits[x % base] + result
        x //= base
    
    return result

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base(x, base)` that converts the number `x` to base `base` and returns the result as a string. The function uses a while loop to repeatedly divide `x` by `base` and prepend the remainder to the result string. The test cases at the end demonstrate the function's behavior with various inputs.