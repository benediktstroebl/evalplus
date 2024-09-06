Here's the code you asked about:
```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of integer x to base base.
    >>> change_base(8, 3) == '22'
    True
    >>> change_base(8, 2) == '1000'
    True
    >>> change_base(7, 2) == '111'
    True
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base value.")
    # Translating base to string representation
    if base == 10:
        base = '0123456789'
    elif base == 12:
        base = '01'
    elif base == 16:
        base = '0123456789abcdef'
    elif base == 22:
        base = '0123456789abcdef}'
    elif base == 23:
        base = '0123456789ABCDEF'
    elif base == 24:
        base = '0123456789ABCDEFGH'
    elif base == 25:
        base = '0123456789ABCDEFGHIJKLMNOPQRSTUV'
    elif base == 26:
        base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif base == 27:
        base = '0123456789ABCDEFGHIJKLMNOPQRSTUVabcdef'
    elif base == 28:
        base = '0123456789ABCDEFGHIJKLMNOPQRSTUVabcdefgh'
    elif base == 29:
        base = '0123456789ABCDEFGHIJKLMNOPQRSTUVabcdefghijklmnop'
    elif base == 30:
        base = '0123456789ABCDEFGHIJKLMNOPQRSTUVabcdefghijklmnnop'
    else:
        raise ValueError("Unsupported base value")
    
    # Applying mathematical operation to convert x to string representation
    x = x % base
    digits = [int(d) for d in str(x, base)]
    return '{:03}'.format(digits)
```
The function `change_base` takes an integer `x` and a base `base` as input and returns the string representation of `x` in the desired base. This code uses the/ mathematical operation to convert `x` to a string using the desired base. The code is self-contained and can be easily imported into other Python scripts to be used.