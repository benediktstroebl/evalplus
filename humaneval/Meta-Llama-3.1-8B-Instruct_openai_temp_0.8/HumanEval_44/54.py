```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The base to convert the number to.
    
    Returns:
    str: The string representation of the number in the new base.
    """
    
    # Check if the base is valid
    if not 2 <= base <= 9:
        raise ValueError("Base must be between 2 and 9")
    
    # Use a list to map digits to their string representations
    digits = "0123456789"
    
    # Initialize the result
    result = ""
    
    # Convert the number to the new base
    while x:
        result = digits[x % base] + result
        x //= base
    
    # Return the result
    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines the `change_base` function to convert a number from base 10 to any base between 2 and 9. It uses a list `digits` to map each digit to its string representation. The number is converted to the new base by repeatedly taking the remainder of the number divided by the base, which gives the last digit in the new base, and then dividing the number by the base to get the remaining digits. The process is repeated until the number is 0. The result is then returned as a string.