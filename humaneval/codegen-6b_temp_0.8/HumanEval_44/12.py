

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
    assert 0 <= x <= 10, 'Base must be between 1 and 10'
    assert 3 <= base <= 9, 'Base must be between 3 and 9'

    # create an empty string to store the converted number
    rep = ''
    while x > 0:
        # convert current number into the current digit
        d = x % base
        # check if the digit is not 9
        if d != 9:
            rep = str(d) + rep
        # update the current number
        x = x//base

    return rep

