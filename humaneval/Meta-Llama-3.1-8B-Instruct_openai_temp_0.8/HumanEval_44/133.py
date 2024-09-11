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
    result = ""

    while x > 0:
        result = convertString[x % base] + result
        x = x // base

    return result


# Test the function
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

This script defines a function `change_base` that takes two integers as input: `x` (the number to convert) and `base` (the target base). It uses a while loop to repeatedly divide `x` by `base` and append the remainder to the result string. The remainders are converted to their corresponding digits using the `convertString` variable. Finally, the function returns the resulting string representation of `x` in the target base.