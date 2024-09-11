```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The target numerical base.
    
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
        raise ValueError("Base should be between 2 and 10")
    
    if x == 0:
        return '0'
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while x > 0:
        x, remainder = divmod(x, base)
        result = digits[remainder] + result
    
    return result

# Test the function
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input. It converts the integer `x` to the target base and returns the string representation of the number in that base. The function uses a while loop to repeatedly divide the input number by the base and append the remainder to the result. It uses a string of digits to map the remainder to the corresponding digit in the target base. The function also includes input validation to check if the base is within the valid range of 2 to 10.