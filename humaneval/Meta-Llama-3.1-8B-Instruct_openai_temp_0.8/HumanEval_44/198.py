```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers are less than 10.

    Args:
        x (int): The input number.
        base (int): The target base.

    Returns:
        str: The string representation of x in base.

    Examples:
        >>> change_base(8, 3)
        '22'
        >>> change_base(8, 2)
        '1000'
        >>> change_base(7, 2)
        '111'
    """
    if x == 0:
        return '0'

    digits = []
    while x:
        digits.append(int(x % base))
        x //= base

    return ''.join(map(str, digits[::-1]))

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` as input. It converts `x` to the specified base and returns the result as a string. The function uses a while loop to repeatedly divide `x` by `base` and append the remainder to the `digits` list. The result is then reversed and joined into a string. The script also includes test cases to verify the correctness of the function.