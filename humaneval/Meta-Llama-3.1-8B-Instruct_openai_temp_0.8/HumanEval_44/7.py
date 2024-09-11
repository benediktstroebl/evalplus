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
        str: The string representation of x in the specified base.

    Example:
        >>> change_base(8, 3)
        '22'
        >>> change_base(8, 2)
        '1000'
        >>> change_base(7, 2)
        '111'
    """
    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)


# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script uses a recursive approach to convert the number to the specified base. The function `change_base` takes two parameters: `x`, the number to be converted, and `base`, the base to convert to. It uses the floor division operator (`//`) to get the quotient and the modulus operator (`%`) to get the remainder. If the quotient is less than the base, it simply returns the remainder as a string. Otherwise, it recursively calls itself with the quotient and the remainder, and then concatenates the results.