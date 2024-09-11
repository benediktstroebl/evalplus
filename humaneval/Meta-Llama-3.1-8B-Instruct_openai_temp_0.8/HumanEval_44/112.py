```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
    x (int): The number to be converted.
    base (int): The target base (less than 10).
    
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
    if base < 2 or base > 10:
        raise ValueError("Base must be between 2 and 10.")
    
    if x == 0:
        return '0'
    
    result = ''
    while x > 0:
        x, remainder = divmod(x, base)
        result = str(remainder) + result
    
    return result

# Test the function
print(change_base(8, 3))   # Output: '22'
print(change_base(8, 2))   # Output: '1000'
print(change_base(7, 2))   # Output: '111'
```

This script first checks if the base is valid (between 2 and 10). Then, it uses a while loop to continuously divide the input number by the target base until the quotient becomes zero. In each iteration of the loop, it appends the remainder to the result string and updates the quotient to the previous quotient divided by the base.