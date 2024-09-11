```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
        x (int): The number to convert.
        base (int): The target base (2-9).

    Returns:
        str: The string representation of x in base.
    """
    if not 2 <= base <= 9:
        raise ValueError("Base must be between 2 and 9")

    if x == 0:
        return '0'

    result = ''
    while x > 0:
        x, remainder = divmod(x, base)
        result = str(remainder) + result

    return result

# Example usage:
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in the target base. The function uses the `divmod` function to perform integer division and find the remainder, effectively converting `x` to the target base while building the string representation. If the input base is invalid (not between 2 and 9), the function raises a `ValueError`.