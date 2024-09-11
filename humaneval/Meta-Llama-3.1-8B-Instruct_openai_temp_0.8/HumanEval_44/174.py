```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.

    :param x: The number to be converted
    :type x: int
    :param base: The base to convert to
    :type base: int
    :return: The converted number as a string
    :rtype: str
    """
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Both x and base must be integers")
    if base < 2 or base > 10:
        raise ValueError("Base must be between 2 and 10")

    if x == 0:
        return '0'

    digits = []
    while x > 0:
        digits.append(int(x % base))
        x //= base

    return ''.join(map(str, digits[::-1]))

# Test cases
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This script defines a function `change_base` that takes an integer `x` and a base `base` (between 2 and 10) as input and returns the string representation of `x` in the given base. It uses a while loop to repeatedly divide `x` by `base` and append the remainder to the result. The result is then returned as a string. If `x` is 0, it directly returns '0'. The script also includes test cases to demonstrate its usage.