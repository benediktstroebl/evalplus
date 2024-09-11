```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The target base.
    
    Returns:
    str: The string representation of x in the target base.
    
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    
    result = ''
    while x:
        x, remainder = divmod(x, base)
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('A') + remainder - 10) + result
    return result

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script uses Python's built-in `divmod` function to get the quotient and remainder of the division of `x` by `base`. If the remainder is less than 10, it is directly converted to a string. If the remainder is 10 or more, it represents the numbers 10-35 (A-Z) and is converted to a string by adding `ord('A') + remainder - 10` to get the corresponding uppercase letter. The result is built from right to left, with the most significant digit added first.