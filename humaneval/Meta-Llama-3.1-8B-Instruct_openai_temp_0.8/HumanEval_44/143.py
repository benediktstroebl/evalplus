```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.

    Args:
        x (int): The number to be converted.
        base (int): The base to convert the number to.

    Returns:
        str: The string representation of the number in the new base.

    Raises:
        ValueError: If base is greater than or equal to 10.
    """
    if base >= 10:
        raise ValueError("Base numbers are less than 10.")

    converted = ""
    while x > 0:
        converted = str(x % base) + converted
        x //= base

    return converted

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines the `change_base` function to convert a number `x` to a new base `base`. It uses a while loop to repeatedly divide `x` by `base` and append the remainder to the front of the `converted` string. The base-10 representation of `x` is converted to the new base and returned as a string. The script also includes docstrings for documentation and includes test cases for validation.