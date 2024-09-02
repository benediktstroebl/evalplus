

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
    result = ''
    if 0 <= x <= 9:
        result = str(x)
    elif 10 <= x <= 35:
        result = chr(ord('A') + x - 10)
    elif 36 <= x <= 62:
        result = chr(ord('a') + x - 36)
    return result
