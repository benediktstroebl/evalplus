```python
def change_base(x: int, base: int):
    """
    Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

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
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

### How it works:

This script uses a while loop to continuously divide the input number `x` by the target base `base`. The remainder of this division is prepended to the list of digits. After each division, the quotient is assigned back to `x`. Once `x` reaches 0, the loop terminates, and the function reverses the list of digits (which now represents the digits of the converted number in reverse order) and joins them together into a string using the `join` function.