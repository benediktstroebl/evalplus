```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Args:
    x (int): The number to be converted.
    base (int): The target base.
    
    Returns:
    str: The string representation of the number in the target base.
    
    Raises:
    ValueError: If the target base is not less than 10.
    """
    if base < 2 or base > 9:
        raise ValueError("Target base must be between 2 and 9.")
    
    if x == 0:
        return '0'
    
    digits = '0123456789'
    result = ''
    while x:
        x, remainder = divmod(x, base)
        result = digits[remainder] + result
    
    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script provides a function `change_base` that takes an integer `x` and a base `base` as inputs, and returns a string representation of `x` in the target base. It handles numbers up to base 9 (since base numbers are less than 10) and includes error checking to ensure the target base is within the valid range. The test cases provided demonstrate the function's usage and expected output.