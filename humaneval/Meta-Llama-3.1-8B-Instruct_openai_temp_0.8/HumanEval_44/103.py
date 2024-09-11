```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.

    Args:
    x (int): The number to be converted.
    base (int): The target numerical base (less than 10).

    Returns:
    str: The string representation of the number x in base base.

    Raises:
    ValueError: If base is not an integer between 2 and 9.
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Both x and base must be integers.")
    if not 2 <= base <= 9:
        raise ValueError("Base must be an integer between 2 and 9.")

    if x == 0:
        return '0'

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while x:
        result = digits[x % base] + result
        x //= base

    return result


# Example usage:
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This Python function `change_base` converts an integer `x` to a specified numerical base `base` (between 2 and 9). The result is returned as a string. If `x` is 0, it directly returns '0'. Otherwise, it repeatedly divides `x` by `base` and prepends the remainder (as a character from '0' to '9' or 'A' to 'Z') to the `result` string.