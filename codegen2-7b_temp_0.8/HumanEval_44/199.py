

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
    if base > 10:
        raise ValueError("Value of base must be less than 10.")
    else:
        if base < 10:
            return str(base * x)
        elif base == 10:
            return str(x)
        else:
            return str(base**x
