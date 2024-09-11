```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The base to which the number is to be converted.
    
    Returns:
    str: The string representation of the number in the new base.
    
    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    convertString = "0123456789"
    result = ""
    while x > 0:
        result = convertString[x % base] + result
        x = x // base
    return result

# Test the function
print(change_base(8, 3))    # Output: '22'
print(change_base(8, 2))    # Output: '1000'
print(change_base(7, 2))    # Output: '111'
```

This script uses a while loop to continuously divide the input number `x` by the base, adding the remainder (which represents the digit in the new base) to the result string. The process repeats until `x` becomes 0. The result string is then returned.