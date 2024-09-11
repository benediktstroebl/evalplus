```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Args:
    x (int): The number to be converted.
    base (int): The target base. Numbers should be less than 10.
    
    Returns:
    str: String representation of the number in the target base.
    
    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    # Handle invalid bases
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")
    
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    # Reverse the list of digits and convert to string
    return ''.join(map(str, digits[::-1]))

# Test cases
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

This script uses a simple conversion algorithm to change the base of a given number `x` to the target base `base`. It handles invalid bases and inputs of zero. The test cases at the end demonstrate the function's usage with the provided examples.