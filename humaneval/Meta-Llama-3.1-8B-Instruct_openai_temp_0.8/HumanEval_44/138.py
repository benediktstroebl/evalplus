```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
        x (int): The number to be converted.
        base (int): The base to convert to.

    Returns:
        str: The string representation of the number in the new base.
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Both x and base must be integers")

    if base < 2 or base > 9:
        raise ValueError("Base must be between 2 and 9")

    if x == 0:
        return '0'

    digits = "0123456789"
    result = ""

    while x > 0:
        result = digits[x % base] + result
        x //= base

    return result

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that takes an integer `x` and an integer `base` as input and returns a string representation of `x` in the new base. The function first checks if both `x` and `base` are integers. It then checks if `base` is within the valid range of 2 to 9. If either of these checks fail, the function raises a `ValueError`. Otherwise, it converts `x` to the new base using the standard algorithm for base conversion and returns the result as a string. The script also includes test cases to verify the correctness of the function.