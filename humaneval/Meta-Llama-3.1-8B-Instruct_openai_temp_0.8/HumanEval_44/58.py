```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
        x (int): Input number.
        base (int): Target base.
        
    Returns:
        str: String representation of x in base base.
    """
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    # Convert list of digits to string
    digits = ''.join(map(str, digits[::-1]))
    
    return digits

# Test cases
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

This script defines a function `change_base` that takes an integer `x` and a target base `base` as input. It then performs the conversion by repeatedly dividing `x` by `base` and appending the remainder to a list of digits. After all divisions are done, it reverses the list of digits and joins them into a string. The function returns this string representation of `x` in base `base`. The test cases at the end verify that the function works as expected.