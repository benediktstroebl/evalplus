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
print(change_base(8, 3))  # '22'
print(change_base(8, 2))  # '1000'
print(change_base(7, 2))  # '111'
```

This Python function `change_base` converts a number from base 10 to any base between 2 and 9 (inclusive). It uses a simple while loop to perform the conversion and then joins the digits together in the correct order to form the final base representation. 

The function takes two arguments: `x` (the number to be converted) and `base` (the base to convert to). It returns a string representation of the number in the desired base. 

Note that if the input number `x` is 0, the function immediately returns '0', since there is no need to perform the conversion.