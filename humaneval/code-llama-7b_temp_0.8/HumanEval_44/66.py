

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

    assert x > 0, "must be positive"
    assert 1 < base < 10, "must be 2-9"

    if x == 1:
        return "1"

    result = ""
    while x > 0:
        y = x % base
        x = x // base
        result = str(y) + result

    return result


