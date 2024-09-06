

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
    ##convert string to integer
    x = int(x)
    ##convert integer to base
    remainder = x % base
    ##convert base to string
    output = ''
    if remainder == 0:
        output = '0'
    while remainder is not 0:
        quotient = x // base
        x = remainder
        remainder = quotient % base
        output = str(remainder) + output
    return output
