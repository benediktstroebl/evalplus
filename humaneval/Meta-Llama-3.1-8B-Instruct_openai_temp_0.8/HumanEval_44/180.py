```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The input number to be converted.
    base (int): The base to convert the number to.
    
    Returns:
    str: The string representation of the number in the new base.
    
    Example:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # Check if the input number is valid
    if x < 0:
        raise ValueError("Input number cannot be negative.")
    
    # Check if the base is valid (less than 10)
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9.")
    
    # Perform the conversion
    if x == 0:
        return '0'
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    return ''.join(map(str, digits[::-1]))

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in base `base`. The function uses a while loop to perform the conversion by repeatedly taking the remainder of `x` divided by `base` and appending it to the list of digits. The loop continues until `x` becomes 0. The digits are then reversed and joined together to form the string representation of the number in the new base.