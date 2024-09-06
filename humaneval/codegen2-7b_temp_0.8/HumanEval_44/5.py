

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
    if base > 10 or base < 2:
        raise ValueError('base value is not between 2 and 10')
    else:
        base_string = ""
        while x >= base:
            base_string += str(x % base)
            x = x // base
        base_string += str(x)
        return base_string
    
