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
    digits = ""
    while x:
        digits = str(x % base) + digits
        x //= base
    return digits

# Test cases
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
```

In this script, we use a while loop to continuously divide the input number `x` by the base and append the remainder to the `digits` string. The loop continues until `x` becomes 0. The result is a string representing the input number in the desired base.