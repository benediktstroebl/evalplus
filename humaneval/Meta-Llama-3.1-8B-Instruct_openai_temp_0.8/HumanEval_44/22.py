```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
        x (int): Input number to change base.
        base (int): Target base for conversion (less than 10).

    Returns:
        str: String representation of x in base.
    """
    if x == 0:
        return '0'
    
    digits = '0123456789ABCDEF'
    result = ''
    
    while x > 0:
        # Get remainder of x divided by base
        remainder = x % base
        
        # Prepend remainder to result
        result = digits[remainder] + result
        
        # Update x for next iteration
        x = x // base
    
    return result


# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This Python script defines the `change_base` function, which takes an integer `x` and a base `base` as input, and returns a string representation of `x` in the target base. The function uses a while loop to repeatedly divide `x` by `base`, appending the remainder to the result string. The `digits` string is used to map remainder values to their corresponding characters (e.g., 0-9 for decimal, A-F for hexadecimal). The script also includes test cases to verify the function's correctness.