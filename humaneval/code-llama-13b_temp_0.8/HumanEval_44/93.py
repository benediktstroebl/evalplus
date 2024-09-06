

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
    x_base10 = 0
    base_counter = 0
    #while x > 0:
    #    x_base10 += x%base*10**base_counter
    #    x = x//base
    #    base_counter += 1
    while x > 0:
        digit = x % base
        x_base10 = x_base10*base + digit
        x = x // base
    return str(x_base10)


