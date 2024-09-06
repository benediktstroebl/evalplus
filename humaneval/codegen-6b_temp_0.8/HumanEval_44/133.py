

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
    # upper case
    if x < 0:
        sign = -1
    else:
        sign = 1
    x *= sign
    convertString = ""
    while x!=0:
        convertString = str(x%base) + convertString
        x //= base
    return convertString if sign == 1 else (convertString[0] + convertString[1:])
