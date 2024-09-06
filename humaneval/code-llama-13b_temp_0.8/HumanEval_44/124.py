

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
    assert 0 <= x, "x should be a positive integer"
    assert base > 0, "base should be a positive integer"
    if x == 0:
        return "0"
    else:
        out = []
        while x > 0:
            out.append(str(x % base))
            x = x // base
        return "".join(reversed(out))

