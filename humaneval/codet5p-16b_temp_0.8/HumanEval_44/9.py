

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

    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    res = ''
    x_mod_base = x % base
    while x_mod_base > 0:
        res = chars[x_mod_base % base] + res
        x_mod_base //= base
    return res if x > 0 else '-' + res
    
    
    
    
