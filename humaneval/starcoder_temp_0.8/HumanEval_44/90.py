

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
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert x >= 0, 'negative numbers not supported: {}'.format(x)
    # TODO: Convert number in the required base
    new_num = ''
    val = x
    while val > 0:
        val, mod = divmod(val, base)
        new_num += string.digits + string.ascii_lowercase[mod]

    return new_num[::-1]

