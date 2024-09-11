```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    
    Args:
        x (int): The number to be converted.
        base (int): The target base (less than 10).
    
    Returns:
        str: The string representation of the number in the target base.
    
    Raises:
        ValueError: If the base is not less than 10.
    """
    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")

    digits = '012345678'
    if x < base:
        return digits[x]
    else:
        return change_base(x // base, base) + digits[x % base]


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This Python function `change_base(x, base)` converts the input integer `x` to the desired base `base`. It recursively divides the input number by the target base and appends the remainder as a string digit to the result. The base cases are when the input number is less than the target base, in which case it returns the string representation of the number directly.

Note that this function raises a `ValueError` if the target base is not between 2 and 9, as required by the problem statement.