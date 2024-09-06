

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
    assert base >= 2 and base <= 10, "invalid base"
    b = bin(x)
    assert b[-1]!= "0", "negative number"
    return b[2:] if base == 10 else str(int(b[2:], base))
