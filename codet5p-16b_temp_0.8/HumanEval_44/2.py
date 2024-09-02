

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

    base_num = change_base.base_numbers[base]
    res = ""
    while x > 0:
        res += str(x % base)
        x //= base
    return res[::-1] or '0'


    2: '01',
    8: '1000',
    10: '0123456789',
    16: '0123456789abcdef',

