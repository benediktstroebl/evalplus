```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
    x (int): The number to be converted.
    base (int): The base to convert the number to. Must be between 2 and 9 (inclusive).
    
    Returns:
    str: The string representation of the number in the new base.
    
    Raises:
    ValueError: If the base is not between 2 and 9 (inclusive).
    
    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if not 2 <= base <= 9:
        raise ValueError("Base must be between 2 and 9 (inclusive).")
    
    # Convert the number to base 10 and then to the desired base
    result = ""
    temp = x
    while temp > 0:
        temp, remainder = divmod(temp, base)
        result = str(remainder) + result
    
    return result

# Test the function
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in the base `base`. It uses the built-in `divmod` function to divide `x` by `base` and get the remainder, and then appends the remainder to the result string in reverse order. The function raises a `ValueError` if the base is not between 2 and 9 (inclusive). The script also includes some test cases to demonstrate the function's behavior.