```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
    x (int): Input number to be converted.
    base (int): Target base for conversion.
    
    Returns:
    str: String representation of the converted number.
    """
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    # Reverse the list of digits and convert to string
    digits.reverse()
    return ''.join(map(str, digits))

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base(x, base)` that takes an integer `x` and a base `base` as input, and returns a string representation of `x` in base `base`. The function uses a while loop to repeatedly divide `x` by `base` and append the remainder to the list of digits. After the loop, the function reverses the list of digits and joins them into a string. The test cases at the end demonstrate the function's correctness.