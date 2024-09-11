```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Args:
        x (int): Number to be converted.
        base (int): Target base (less than 10).
    
    Returns:
        str: String representation of x in base.
    
    Example:
        >>> change_base(8, 3)
        '22'
        >>> change_base(8, 2)
        '1000'
        >>> change_base(7, 2)
        '111'
    """
    convertString = "0123456789ABCDEF"
    result = ""
    
    # Check for valid base
    if base < 2 or base > 16:
        raise ValueError("Base must be between 2 and 16")
    
    # Perform conversion
    while x > 0:
        remainder = x % base
        result = convertString[remainder] + result
        x = x // base
    
    return result

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```
This script defines the `change_base` function which performs the conversion from a decimal number to any base between 2 and 16. The function uses a string of digits and alphabets to represent the base numbers. The while loop continuously divides the input number by the target base and prepends the remainder to the result string. The function then returns the result string after the conversion. The script includes comments, docstrings, and test cases to demonstrate its functionality.