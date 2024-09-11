```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if not isinstance(x, int) or not isinstance(base, int) or base < 2 or base >= 10:
        raise ValueError("Invalid base or input number")

    if x == 0:
        return '0'

    digits = '0123456789'
    result = ''

    while x > 0:
        result = digits[x % base] + result
        x //= base

    return result


# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that converts an integer `x` to a specified base `base`, with the constraint that `base` should be less than 10. The function handles integers 0 through 9 as the digits 0-9 in the new base, and raises a ValueError if `base` is not valid.

The function works by repeatedly taking the remainder of `x` divided by `base` (which gives the next digit in the new base), subtracting the remainder from `x` (which effectively divides `x` by `base`), and prepending the digit to the result string. This process continues until `x` is 0, at which point the final result string is returned.

The test cases demonstrate the function's behavior with the specified inputs.