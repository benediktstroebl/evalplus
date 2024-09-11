```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    
    # Special case: if x is 0, return '0' regardless of the base
    if x == 0:
        return '0'
    
    # Convert x to the desired base
    digits = '0123456789'
    if base < 2 or base >= 10:
        raise ValueError("Base must be between 2 and 9")
    
    result = ''
    while x > 0:
        # Get the remainder of x divided by base
        remainder = x % base
        # Prepend the corresponding digit to the result
        result = digits[remainder] + result
        # Update x to be the quotient of x divided by base
        x //= base
    
    return result

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in the desired base. The function works by repeatedly dividing `x` by `base` and prepending the corresponding digit to the result. The function also handles the special case where `x` is 0. The script includes several test cases to verify that the function works correctly.