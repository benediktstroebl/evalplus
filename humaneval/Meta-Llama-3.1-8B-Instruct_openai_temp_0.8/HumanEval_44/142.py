```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
    x (int): The number to be converted.
    base (int): The target base of the conversion.
    
    Returns:
    str: The string representation of the number x in base base.
    """
    
    # Handle special cases
    if x == 0:
        return '0'
    
    # Initialize an empty string to store the result
    result = ''
    
    # Use a while loop to perform the conversion
    while x > 0:
        # Calculate the remainder of x divided by base
        remainder = x % base
        
        # Append the remainder to the result (as a string)
        result = str(remainder) + result
        
        # Update x by performing integer division by base
        x = x // base
    
    return result


# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that takes two integer arguments `x` and `base` and returns a string representation of `x` in base `base`. The function uses a while loop to repeatedly divide `x` by `base` and append the remainder to the result string. The result is then returned.