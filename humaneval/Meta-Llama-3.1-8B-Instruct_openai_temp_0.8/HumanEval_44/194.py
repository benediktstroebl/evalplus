```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    Args:
        x (int): Number to be converted.
        base (int): Target base.

    Returns:
        str: String representation of x in base.
    """
    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)


# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a recursive function `change_base` to convert a number `x` to a target base `base`. It uses integer division (`//`) to get the quotient and modulo operator (`%`) to get the remainder of `x` divided by `base`. If `x` is less than `base`, it simply converts `x` to a string and returns it. Otherwise, it recursively converts the quotient and appends the remainder as a string.