

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
    # base 10
    if base < 10:
        return str(x)
    # if base is greater than 10, we return the number in the base 10
    # form of the base.
    else:
        return str(int(x) * (10 ** len(str(x)) - 1) // (base - 1))
