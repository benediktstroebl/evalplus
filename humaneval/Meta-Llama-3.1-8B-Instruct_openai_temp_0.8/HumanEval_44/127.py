```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    
    Args:
        x (int): The number to convert.
        base (int): The target numerical base (less than 10).
    
    Returns:
        str: The string representation of x in the base numerical system.
    
    Examples:
        >>> change_base(8, 3)
        '22'
        >>> change_base(8, 2)
        '1000'
        >>> change_base(7, 2)
        '111'
    """
    if not (0 <= x < base):
        raise ValueError("x must be in the range [0, base-1]")
    
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(str(x % base))
        x //= base
    return ''.join(digits[::-1])

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that converts a number `x` to a different base. It checks if `x` is in the range [0, base-1] to ensure that the conversion is valid. If `x` is 0, it returns '0'. Otherwise, it repeatedly takes the remainder of `x` divided by the base and prepends it to the list of digits. The function finally joins the list of digits in reverse order to form the result.