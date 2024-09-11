```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The base to which the number is to be converted.
    
    Returns:
    str: The string representation of the number in the specified base.
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Both x and base must be integers.")
    if base < 2 or base > 10:
        raise ValueError("Base must be between 2 and 10 (inclusive).")
    
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    # Reverse the list of digits
    digits.reverse()
    
    # Convert digits to string
    return ''.join(map(str, digits))

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script uses a simple method to convert the number from base 10 to the specified base. It repeatedly finds the remainder of the number when divided by the base, and then divides the number by the base. The remainders are stored in a list. After the number is converted to the specified base, the list of remainders is reversed and joined together to form the final result.