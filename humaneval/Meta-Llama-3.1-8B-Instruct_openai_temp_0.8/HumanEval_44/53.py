```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Parameters:
    x (int): The number to convert.
    base (int): The base to convert to.
    
    Returns:
    str: The string representation of x in the given base.
    """
    # Handle the case when x is 0
    if x == 0:
        return '0'
    
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    
    # Reverse the list of digits and convert to string
    return ''.join(map(str, reversed(digits)))

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns its string representation in the given base. The function uses a while loop to repeatedly divide the input number by the base and append the remainder to a list of digits. Finally, it reverses the list of digits and joins them together into a string. The test cases at the end demonstrate the function's correctness.