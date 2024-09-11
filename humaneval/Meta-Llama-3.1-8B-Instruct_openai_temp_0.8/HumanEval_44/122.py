```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The base to convert to (less than 10).
    
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
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    # Reverse the list of digits and convert to string
    return ''.join(map(str, digits[::-1]))

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines the `change_base` function to convert a number `x` to a specific base `base`. It works by continuously taking the remainder of `x` when divided by `base` (the last digit in the new base), and then dividing `x` by `base` to move to the next digit. The process repeats until `x` becomes 0. The digits are then reversed and converted to a string, with each digit represented as a string.