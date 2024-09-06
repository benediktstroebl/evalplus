

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
    assert type(x) == int and x > 0 and base < 10, 'Illegal Argument'
    if x == 0:
        return str([])
    res = []
    convert_n = 10
    while x > 0:
        y = x % convert_n
        res.append(str(y))
        x = x // convert_n
        if x == 0:
            break
        convert_n *= base
    return ''.join(res[::-1])
