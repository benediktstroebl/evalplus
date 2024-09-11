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
    
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = ''
    
    while x:
        result = digits[x % base] + result
        x //= base
    
    return result

# Test the function
print(change_base(8, 3))  # Output: 22
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
```

In this script, we define a function `change_base` that takes an integer `x` and a base `base` as arguments. The function uses a while loop to repeatedly divide `x` by `base` and append the remainder to the result string. The remainder is obtained using the modulus operator (`x % base`), and the result is prepended to the `result` string. The loop continues until `x` becomes 0. We use a string `digits` to map the remainder to a digit or a letter representing the digit in the new base.