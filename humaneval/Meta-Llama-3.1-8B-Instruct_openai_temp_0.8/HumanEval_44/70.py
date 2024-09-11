```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The target base.
    
    Returns:
    str: The string representation of x in the target base.
    """
    if x == 0:
        return '0'
    
    digits = '0123456789'
    result = ''
    
    while x > 0:
        result = digits[x % base] + result
        x //= base
    
    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that converts a given integer `x` to a specified base `base`. It uses a while loop to continuously divide `x` by `base` and append the remainder to the `result` string, which is then returned as the string representation of `x` in the target base. The test cases at the end demonstrate the function's usage and correctness.