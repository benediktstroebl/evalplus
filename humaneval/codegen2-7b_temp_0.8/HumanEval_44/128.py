

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
    conversion = {
        '01': 2,
        '02': 8,
        '03': 16,
        '04': 10,
    }
    x_str = str(x)
    res = ''
    for i in x_str:
        res += conversion.get(i)
    return
