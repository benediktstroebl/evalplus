

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

    assert isinstance(x, int)
    assert isinstance(base, int)
    assert base >= 10
    digits = change_base.num_digits(x, base)
    base_rep = change_base.convert_base(x, base)
    return change_base.pad_rep(digits, base_rep)


