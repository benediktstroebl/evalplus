```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
        x (int): The number to convert.
        base (int): The base to convert to.

    Returns:
        str: The string representation of the number in the new base.
    """
    if x == 0:
        return '0'
    
    digits = '0123456789'
    convert_string = ''
    while x > 0:
        convert_string = digits[x % base] + convert_string
        x = x // base
    return convert_string

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input and returns the string representation of `x` in the new base. The function uses a while loop to repeatedly divide `x` by `base` and append the remainder to the convert string. The remainder is converted to a digit using the string `digits`, which contains the digits 0-9. The function handles the base case where `x` is 0 by returning '0'. The script also includes test cases to verify the function's correctness.