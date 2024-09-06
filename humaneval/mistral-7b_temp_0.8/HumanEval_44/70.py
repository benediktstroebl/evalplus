

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
    result = ''
    if x == 0:
        result = '0'
    while x > 0:
        remain = x % base
        if remain > 9:
            remain = chr(remain - 10 + ord('A'))
        result = remain + result
        x = x // base
    return result
