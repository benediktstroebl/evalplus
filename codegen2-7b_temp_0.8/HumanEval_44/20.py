

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
    if base >= 10:
        raise Exception("Base is too large.")
    if base == 1:
        return str(x)
    if base == 0:
        raise Exception("Base is too small.")
    if x == 0:
        return "0"
    return "{0:d}".format(x).replace("0", "0")
