```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    :param x: The number to be converted
    :type x: int
    :param base: The target base
    :type base: int
    :return: String representation of x in base
    :rtype: str
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Both x and base must be integers")
    if base < 2 or base > 9:
        raise ValueError("Target base must be between 2 and 9 (inclusive)")

    num_str = ''
    while x > 0:
        num_str = str(x % base) + num_str
        x //= base

    return num_str

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script includes the function `change_base(x, base)` that takes an integer `x` and a base `base` and returns the string representation of `x` in the target base. It handles base conversion by continuously dividing the input number by the target base and appending the remainder to the result. It also includes input validation to ensure that `x` and `base` are integers and that `base` is between 2 and 9 (inclusive).