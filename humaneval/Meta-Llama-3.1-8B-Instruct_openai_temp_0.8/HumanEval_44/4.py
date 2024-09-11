```python
def change_base(x: int, base: int) -> str:
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    Args:
        x (int): Number to be converted.
        base (int): Target base.

    Returns:
        str: String representation of number in target base.

    Example:
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


# Test cases
print(change_base(8, 3))   # Output: 22
print(change_base(8, 2))   # Output: 1000
print(change_base(7, 2))   # Output: 111
```

This Python script defines a function `change_base(x, base)` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in base `base`. The function uses a while loop to repeatedly divide `x` by `base` and append the remainder to the list of digits. The digits are then reversed and joined together to form the final string representation. The script includes example test cases to demonstrate the function's behavior.