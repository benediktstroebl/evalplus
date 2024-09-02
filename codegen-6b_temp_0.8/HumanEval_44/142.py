

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
    if x < 10:
        return str(x)
    elif x == 10:
        return '1'
    elif x == 11:
        return 'a'
    elif x == 12:
        return 'b'
    elif x == 13:
        return 'c'
    elif x == 14:
        return 'd'
    elif x == 15:
        return 'e'
    elif x == 16:
        return 'f'
    elif x == 17:
        return 'g'
    elif x == 18:
        return 'h'
    elif x == 19:
        return 'i'
    elif x == 20:
        return 'j'
    elif x == 21:
        return 'k'
    elif x == 22:
        return 'l'
    elif x == 23:
        return 'm'
    elif x == 24:
        return 'n'
    elif x == 25:
        return 'o'
    elif x == 26:
        return 'p'
    elif x == 27:
        return 'q'
    elif x == 28:
        return 'r'
    elif x == 29:
        return 's'
    elif x == 30:
        return 't'
    elif x == 31:
        return 'u'
    elif x == 32:
        return 'v'
    elif x == 33:
        return 'w'
    elif x == 34:
        return 'x'
    elif x == 35:
        return 'y'
    elif x == 36:
        return 'z'
    elif x == 37:
        return '1'
    elif x == 38:
        return '2'
    elif x == 39:
        return '3'
    elif x == 40:
        return '4'
    elif x == 41:
        return '5'
    elif x == 42:
        return '6'
    elif x == 43:
        return '7'
    elif x == 44:
        return '8'
    elif x == 45:
