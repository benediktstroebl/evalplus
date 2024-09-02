

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
    if base < 2 or base > 36:
        raise ValueError('base must be >= 2 and < 36')
    
    if base == 10:
        return str(x)
    
    digits = [str(x % 10)]
    x /= 10
    while x > 0:
        digits.append(str(x % base))
        x /= base
    return ''.join(digits[::-
