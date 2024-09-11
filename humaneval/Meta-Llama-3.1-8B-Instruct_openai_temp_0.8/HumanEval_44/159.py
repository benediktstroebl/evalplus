```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
        x (int): The number to convert.
        base (int): The base to convert to.

    Returns:
        str: The string representation of the number in the new base.
    """
    if base < 2 or base > 10:
        raise ValueError("Base must be between 2 and 10")

    digits = "0123456789"
    result = ""

    while x > 0:
        result = digits[x % base] + result
        x = x // base

    return result

# Example usage:
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines the `change_base` function that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in the new base. The function handles bases between 2 and 10, and raises a `ValueError` for other bases. The example usage at the end demonstrates how to use the function.