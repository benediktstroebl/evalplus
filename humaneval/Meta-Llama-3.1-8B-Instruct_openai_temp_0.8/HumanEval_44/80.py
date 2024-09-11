```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Args:
    x (int): The number to convert.
    base (int): The base to convert to.
    
    Returns:
    str: String representation of the converted number.
    
    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    
    # Handle invalid bases
    if not 2 <= base <= 9:
        raise ValueError("Invalid base. Base must be between 2 and 9.")
    
    # Handle negative numbers
    if x < 0:
        sign = '-'
        x = -x
    else:
        sign = ''
    
    # Convert to the desired base
    result = ''
    while x:
        x, remainder = divmod(x, base)
        result = str(remainder) + result
    
    # Add the sign if necessary
    return sign + result

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes two arguments, `x` and `base`, and returns a string representation of `x` in base `base`. The function first checks if the base is valid, then handles negative numbers, and finally converts `x` to the desired base using a while loop and the `divmod` function. The result is then returned with the appropriate sign if the original number was negative.