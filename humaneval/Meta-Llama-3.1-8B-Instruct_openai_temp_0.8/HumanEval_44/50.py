```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Args:
    x (int): The number to be converted.
    base (int): The base to convert the number to. 
                base numbers are less than 10.
    
    Returns:
    str: String representation after the conversion.
    
    Example:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    convertString = "0123456789"
    result = ''
    while x > 0:
        result = convertString[x % base] + result
        x = x // base
    return result

# Test cases
print(change_base(8, 3))  # Expected output: '22'
print(change_base(8, 2))  # Expected output: '1000'
print(change_base(7, 2))  # Expected output: '111'
```

This script defines a function `change_base` that converts a given integer `x` to a specified base. The function uses a while loop to continuously divide the input number by the specified base and append the remainder (which corresponds to the digit in the new base) to the result string. The base is limited to less than 10 since the problem statement mentioned base numbers less than 10. The script includes test cases at the end to demonstrate the function's usage.