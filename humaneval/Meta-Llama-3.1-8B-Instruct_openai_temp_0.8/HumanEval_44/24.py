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
    convertString = "0123456789"
    if x < base:
        return convertString[x]
    else:
        return change_base(x // base, base) + convertString[x % base]


# Test cases
print(change_base(8, 3))  # Expected output: '22'
print(change_base(8, 2))  # Expected output: '1000'
print(change_base(7, 2))  # Expected output: '111'
print(change_base(10, 2))  # Expected output: '1010'
print(change_base(16, 2))  # Expected output: '10000'
```

This script uses a recursive function to perform the base conversion. The function takes an integer `x` to be converted and a base `base` as parameters. It uses a string `convertString` to map the integers 0-9 to their corresponding digits in the converted base. If `x` is less than the base, it simply returns the corresponding digit from the string. Otherwise, it recursively calls itself with `x // base` (integer division) and appends the digit corresponding to `x % base` (remainder of `x / base`) to the result.