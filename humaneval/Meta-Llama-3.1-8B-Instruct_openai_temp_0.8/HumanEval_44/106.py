```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
        x (int): The number to convert.
        base (int): The target numerical base.

    Returns:
        str: The string representation of the number in the target base.

    Example:
        >>> change_base(8, 3)
        '22'
        >>> change_base(8, 2)
        '1000'
        >>> change_base(7, 2)
        '111'
    """
    # Check if the base is valid
    if not 2 <= base <= 9:
        raise ValueError("Base must be between 2 and 9")

    # Convert the number to the target base using recursion
    def convert(n, base):
        if n < base:
            return str(n)
        else:
            return convert(n // base, base) + str(n % base)

    return convert(x, base)

# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input, and returns the string representation of `x` in the target base. The function first checks if the base is valid, and then uses a recursive helper function `convert` to perform the conversion. The script also includes example use cases at the end.