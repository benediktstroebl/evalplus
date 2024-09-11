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
    
    digits = []
    while x > 0:
        digits.append(str(x % base))
        x //= base
    
    return ''.join(reversed(digits))


# Example usage
print(change_base(8, 3))    # Output: '22'
print(change_base(8, 2))    # Output: '1000'
print(change_base(7, 2))    # Output: '111'
print(change_base(10, 2))   # Output: '1010'
```

This script defines a function `change_base` that takes an integer `x` and a base number `base` as input. It uses a loop to keep track of the remainder of `x` divided by `base`, which represents the next digit in the new base. This process continues until `x` becomes 0. The digits are then collected and joined together to form the string representation in the new base.