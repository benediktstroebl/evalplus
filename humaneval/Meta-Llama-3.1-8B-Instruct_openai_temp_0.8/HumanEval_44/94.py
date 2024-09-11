```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
        x (int): The number to be converted.
        base (int): The target base of the number.
        
    Returns:
        str: String representation of the number in the target base.
    """
    digits = "0123456789"
    if x < base:
        return digits[x]
    else:
        return change_base(x // base, base) + digits[x % base]

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script uses a recursive approach to convert a decimal number to any base less than 10. The function `change_base` takes two arguments: `x` (the decimal number to be converted) and `base` (the target base). It uses a string of digits to represent the possible digits in the target base. If the number to be converted is less than the target base, it returns the corresponding digit from the string of digits. Otherwise, it recursively converts the quotient of the number divided by the target base and appends the remainder (which is a digit in the target base) to the result.