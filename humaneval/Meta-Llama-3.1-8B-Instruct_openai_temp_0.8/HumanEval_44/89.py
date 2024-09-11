### Numerical Base Conversion Function
```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Args:
        x (int): The number to convert.
        base (int): The target base.
    
    Returns:
        str: The string representation of x in base.
    
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
    
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while x > 0:
        result = digits[x % base] + result
        x //= base
    
    return result

# Test the function
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```
This script defines the `change_base` function, which takes an integer `x` and a base `base` as input, and returns the string representation of `x` in the specified base. The function uses the modulo operator (`%`) to get the remainder of `x` divided by `base`, and the floor division operator (`//`) to get the quotient. It then prepends the corresponding digit from the `digits` string to the `result` string for each iteration. The function uses the `while` loop to continue until `x` is 0, at which point it returns the `result` string. The script also includes test cases to demonstrate the function's usage.