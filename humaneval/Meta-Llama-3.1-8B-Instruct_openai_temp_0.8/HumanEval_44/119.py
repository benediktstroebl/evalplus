```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Args:
    x (int): The input number to be converted.
    base (int): The base to convert to.
    
    Returns:
    str: The string representation of x in base.
    
    Raises:
    ValueError: If the base is not less than 10.
    
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if base < 2 or base >= 10:
        raise ValueError("Base should be between 2 and 9.")
    
    convertString = "0123456789ABCDEF"
    result = ""
    
    while x > 0:
        result = convertString[x % base] + result
        x = x // base
    
    return result

# Test cases
print(change_base(8, 3))  # Outputs: 22
print(change_base(8, 2))  # Outputs: 1000
print(change_base(7, 2))  # Outputs: 111
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in base. The function uses the standard method of converting a number from one base to another by continuously dividing the number by the base and appending the remainder to the result. If the base is not less than 10, it raises a `ValueError`. The test cases are included at the end to verify the correctness of the function.