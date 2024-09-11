```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Args:
    x (int): Number to be converted.
    base (int): New base for number x.
    Returns:
    str: String representation of number x after conversion.
    """
    # Create a string of valid digits for the new base
    valid_digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # Handle the case when x is 0
    if x == 0:
        return '0'
    
    # Initialize an empty string to store the result
    result = ''
    
    # Perform the base conversion
    while x:
        result = valid_digits[x % base] + result
        x //= base
    
    return result

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script uses the standard mathematical approach to base conversion, repeatedly dividing the input number by the new base and appending the remainder to the result string. The valid digits are represented as a string, allowing for bases up to 36. The test cases are included at the end of the script to verify its correctness.