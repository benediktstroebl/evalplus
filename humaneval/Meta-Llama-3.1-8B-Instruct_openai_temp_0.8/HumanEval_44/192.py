```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
        x (int): The number to convert.
        base (int): The target base.

    Returns:
        str: The string representation of the number in the target base.
    """
    if not 2 <= base <= 9:
        raise ValueError("Base must be between 2 and 9")

    digits = "012345678"
    if x < base:
        return digits[x]

    result = ""
    while x:
        result = digits[x % base] + result
        x //= base

    return result

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that converts a given integer `x` to a specified base `base`. It uses a while loop to repeatedly divide the input number by the target base and append the remainder to the result. The remainders are used as indices into a string of digits, allowing us to convert the result to the desired base. The function raises a `ValueError` if the target base is not between 2 and 9.