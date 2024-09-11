```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The target base.
    
    Returns:
    str: The string representation of x in the target base.
    """
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    # Convert the list of digits to a string
    digits.reverse()
    return ''.join(map(str, digits))


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
print(change_base(10, 2))  # Output: '1010'
print(change_base(0, 10))  # Output: '0'
```

This script uses a simple iterative approach to convert a number from base 10 to the target base. It repeatedly divides the number by the target base and appends the remainder to the list of digits. The list of digits is then converted to a string and returned. The test cases demonstrate the function's behavior for different inputs.