

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

    #Base value error exception
    if base < 2 or base > 10:
        raise ValueError

    #Value error exception if x is negative
    if x < 0:
        raise ValueError

    #Base case:
    if x < base:
        return str(x)

    #General case:
    else:
        return change_base(x // base, base) + str(x % base)
