```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Args:
    x (int): Input number to be converted.
    base (int): Target base for conversion (less than 10).
    
    Returns:
    str: String representation of the input number in the target base.
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError('Input x and base must be integers.')
    if base < 2 or base >= 10:
        raise ValueError('Base must be between 2 and 9 (inclusive).')

    convertString = "0123456789"
    result = ''

    while x > 0:
        result = convertString[x % base] + result
        x = x // base

    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```
This script defines a function `change_base` that takes an integer `x` and a base `base` (an integer between 2 and 9) as input, and returns the string representation of `x` in the target base. The script also includes test cases to demonstrate the function's correctness.