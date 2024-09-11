```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    :param x: The number to be converted
    :param base: The base to convert to
    :return: The string representation of the number in the new base
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Input must be integers")
    if not 2 <= base <= 9:
        raise ValueError("Base must be between 2 and 9")

    if x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)


# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a recursive function `change_base(x, base)` that converts a number `x` from base 10 to a target base `base`. It recursively divides `x` by `base` and appends the remainder to the result. The function also includes input validation to ensure that `x` and `base` are integers and that `base` is between 2 and 9.