

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
    assert 2 <= base <= 10, 'base out of range: {}'.format(base)

    if x < 10:
        return str(x)

    result = []
    while x:
        x, mod = divmod(x, base)
        result.append(str(mod))
    return ''.join(reversed(result))
