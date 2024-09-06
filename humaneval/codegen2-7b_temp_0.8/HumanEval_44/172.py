

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
    ch_base = {
        0: '0',
        1: '1',
        2: '10',
        3: '11',
        4: '100',
        5: '101',
        6: '1110',
        7: '1111',
        8: '1000',
        9: '1001'
    }
    return str(base) + ch_base[x % base
