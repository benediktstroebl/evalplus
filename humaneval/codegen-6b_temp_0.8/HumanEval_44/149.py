

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
    if x < 0:
        x = abs(x)
        negative = True
    else:
        negative = False
    result = ""
    while x > 0:
        digit = x % base
        if digit < 10:
            result = str(digit) + result
        else:
            result = chr(ord('A') + digit - 10) + result
        x = x // base
    if negative:
        return "-" + result
    else:
        return result
