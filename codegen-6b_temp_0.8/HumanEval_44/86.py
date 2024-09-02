

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
    new_base = x
    if x < 10:
        return str(x)
    else:
        while new_base > 2:
            new_base = new_base / 10
            quotient = new_base
        if new_base == 2:
            return str(x)
        elif new_base == 1:
            return str(x) + '0'
        else:
            residue = x % quotient
            if residue == 0:
                return change_base(x, quotient)
            else:
                return change_base(x, quotient) + str(residue)

