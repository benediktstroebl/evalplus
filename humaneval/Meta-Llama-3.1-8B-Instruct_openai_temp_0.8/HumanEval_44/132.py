```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The target base (less than 10).
    
    Returns:
    str: The string representation of x in base.
    
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
        result = str(x % base) + result
        x //= base
    
    return result

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

In this code, the `change_base` function uses a while loop to continuously divide the input number `x` by the target base `base` and prepend the remainder to the result string. The process continues until `x` is 0, at which point the result string is returned. The test cases at the end demonstrate the function's correctness.