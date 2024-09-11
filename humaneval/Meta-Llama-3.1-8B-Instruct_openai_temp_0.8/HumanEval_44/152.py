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
    str: The string representation of x in base.
    
    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    digits = []
    while x:
        digits.append(int(x % base))
        x //= base
    return ''.join(map(str, digits[::-1]))

# Test the function
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

This script defines the `change_base` function as specified. It converts a number `x` to a new base `base` and returns the result as a string. The function uses a while loop to repeatedly divide `x` by `base` and append the remainder to the result list. The result is then reversed and joined into a string. The script also includes test cases to demonstrate the function's correctness.