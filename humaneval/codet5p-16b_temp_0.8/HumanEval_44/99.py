

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

    power = 0
    string_rep = ''
    while x // base ** power > 0:
        string_rep += str(x // base ** power)
        power += 1
    return string_rep[::-1]

