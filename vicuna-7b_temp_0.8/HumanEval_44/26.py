

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
    # base 2
    if base == 2:
        return str(x)
    
    # base 10
    if base < 10:
        return str(x)
    
    # compute digits
    digits = []
    while x > 0:
        digits.append(x % base)
        x //= base
    
    # join digits to string
    string_digits = ''.join(str(d) for d in digits)
    
    # convert back to number
    x = 0
    for d in string_digits:
        x = x*base + (x >= d)
    
    # return converted string
    return str(x)
