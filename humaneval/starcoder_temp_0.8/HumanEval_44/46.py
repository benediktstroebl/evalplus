

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

    assert base > 1 and base <= 10

    out = ""

    while x > 0:
        q, r = divmod(x, base)
        out += str(r)
        x = q

    return out[::-1]
