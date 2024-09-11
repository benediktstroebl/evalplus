```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Parameters:
    x (int): The number to be converted.
    base (int): The target base for the conversion.

    Returns:
    str: The string representation of x in the base.

    Examples:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Both x and base must be integers.")
    if x < 0 or base < 2 or base > 10:
        raise ValueError("x must be a non-negative integer, and base must be within 2-10.")

    convertString = "0123456789"
    result = ""

    while x > 0:
        result = convertString[x % base] + result
        x = x // base

    return result

# Test the function
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

This script defines a function `change_base(x, base)` that converts the number `x` to the target base `base`. It uses a while loop to repeatedly divide `x` by `base` and append the remainder to the result string. The result string is then returned. The function also includes error checking to ensure that `x` is a non-negative integer and `base` is within the valid range.