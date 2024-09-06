

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
    assert int(x) > 0
    assert base > 1

    if base == 10:
        return str(int(x))

    if x < 26:
        return chr(ord('a') + x - 1)

    if x < 27:
        return chr(ord('A') + x - 26)

    if x < 65:
        return chr(ord('@') + x - 26)

    if x < 97:
        return chr(ord('Z') + x - 26)

    return str(x)

