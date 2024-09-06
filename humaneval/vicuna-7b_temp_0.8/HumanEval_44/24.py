

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
    if base < 10:
        if x > 0:
            return str(x * (10 ** (len(str(base)) - 1)) // (10 ** len(str(base)))) + str(base)
        else:
            return str(x * (10 ** (len(str(base)) - 1)) // (10 ** len(str(base)))) + str(base)
    else:
        return f"{x}X{base}" if x > 0 else f"{x}X{base}0"
