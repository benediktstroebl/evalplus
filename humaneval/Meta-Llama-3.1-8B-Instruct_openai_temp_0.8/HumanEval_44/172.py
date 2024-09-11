```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The number to convert
    base (int): The base to convert to
    
    Returns:
    str: The string representation of the number in the new base
    
    Example:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    
    digits = '0123456789'
    result = ''
    
    while x > 0:
        # Get the remainder of the division of x by base
        remainder = x % base
        # Prepend the corresponding digit to the result
        result = digits[remainder] + result
        # Update x to be the quotient of the division of x by base
        x = x // base
    
    return result

# Example usage:
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input. It then converts `x` to the new base by repeatedly dividing it by `base` and prepending the corresponding digit to the result string. The function returns the resulting string representation of the number in the new base. The example usage at the end shows how to use the function with different inputs.