

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

    """
    # convert x to string of base 10
    string_base_10 = ''
    while x > 0:
        r = x % base
        string_base_10 = str(r) + string_base_10
        x = x // base
    # convert string of base 10 to base 'base'
    string_base = ''
    for i in range(0, len(string_base_10)):
        string_base = str(int(string_base_10[i]) * (base ** i)) + string_base
    return string_base
    """

    string_base = ''
    while x > 0:
        r = x % base
        string_base = str(r) + string_base
        x = x // base
    return string_base

