```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
    x (int): The number to be converted.
    base (int): The base to convert to.
    
    Returns:
    str: The string representation of the number in the new base.
    """
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    # Reverse the list of digits
    digits = digits[::-1]
    
    # Convert the digits to their corresponding characters
    result = ''.join(str(digit) for digit in digits)
    
    return result

# Test cases
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in the new base. The function uses a while loop to repeatedly divide `x` by the base and append the remainder to the list of digits. The digits are then reversed and converted to their corresponding characters. The script also includes test cases to demonstrate the function's correctness.