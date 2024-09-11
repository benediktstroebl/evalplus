```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Parameters:
    x (int): The number to be converted
    base (int): The base to convert the number to
    
    Returns:
    str: The string representation of x in base
    
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
    nums = []
    while x:
        nums.append(int(x % base))
        x //= base
    return ''.join(map(str, nums[::-1]))

# Test the function
print(change_base(8, 3))   # Output: 22
print(change_base(8, 2))   # Output: 1000
print(change_base(7, 2))   # Output: 111
```

This Python script defines a function `change_base` that takes an integer `x` and a base `base` as input and returns a string representation of `x` in the given base. The script then tests the function with the given examples. It recursively divides the input number by the base and appends the remainder to the result, effectively changing the base of the number.