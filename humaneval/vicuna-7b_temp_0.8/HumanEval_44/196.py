

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
    if base == 10:
        return str(x)

    if base == 2:
        return str(x) + "B"

    if base == 3:
        return str(x) + "C"

    if base == 4:
        return str(x) + "D"

    if base == 5:
        return str(x) + "E"

    if base == 6:
        return str(x) + "F"

    if base == 7:
        return str(x) + "G"

    if base == 8:
        return str(x) + "H"

    if base == 9:
        return str(x) + "I"

    if base == 10:
        return str(x) + "J"

    if base == 11:
        return str(x) + "K"

    if base == 12:
        return str(x) + "L"

    if base == 13:
        return str(x) + "M"

    if base == 14:
        return str(x) + "N"

    if base == 15:
        return str(x) + "O"

    return "P"
