```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted.
    base (int): The target base.
    
    Returns:
    str: The string representation of the number in the target base.
    
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    result = ''
    while x > 0:
        x, remainder = divmod(x, base)
        result = str(remainder) + result
    return result

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines the `change_base` function that takes an integer `x` and a base `base` as input, converts `x` to the target base, and returns the result as a string. The function uses a while loop and the `divmod` function to perform the conversion. The test cases are included at the end of the script to verify the function's correctness.