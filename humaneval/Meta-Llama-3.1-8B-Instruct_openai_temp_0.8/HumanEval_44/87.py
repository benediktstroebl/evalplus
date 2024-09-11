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
    if x == 0:
        return '0'
    
    result = ''
    while x > 0:
        x, remainder = divmod(x, base)
        result = str(remainder) + result
    
    return result

# Test cases
print(change_base(8, 3))  # Expected output: 22
print(change_base(8, 2))  # Expected output: 1000
print(change_base(7, 2))  # Expected output: 111
print(change_base(16, 2)) # Expected output: 10000
```

In this script, the `divmod` function is used to get both the quotient and remainder of the division of `x` by `base` in a single operation. The remainder is converted to a string and prepended to the `result` string in each iteration. This process continues until `x` becomes 0. At that point, `result` contains the base-10 representation of the input number in base `base`, which is then returned.