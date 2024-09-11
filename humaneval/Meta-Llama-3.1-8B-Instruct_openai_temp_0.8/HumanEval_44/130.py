```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The target base.
    
    Returns:
    str: The string representation of the number in the target base.
    """
    
    if x == 0:
        return '0'
    
    digits = ''
    while x > 0:
        x, remainder = divmod(x, base)
        digits = str(remainder) + digits
    
    return digits

# Test the function
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in the target base. The function works by repeatedly dividing `x` by `base` and appending the remainder to the string `digits`. The process continues until `x` is 0. If `x` is 0, the function returns '0' immediately.

The script then tests the function with the provided examples.