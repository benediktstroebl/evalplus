```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
    x (int): The number to be converted.
    base (int): The target base for the conversion.

    Returns:
    str: The string representation of x in the target base.
    """
    # Handle edge cases where base is 1 or x is 0
    if base < 2 or x == 0:
        return str(x)

    digits = "0123456789"
    if x < base:
        return digits[x]
    else:
        return change_base(x // base, base) + digits[x % base]


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```