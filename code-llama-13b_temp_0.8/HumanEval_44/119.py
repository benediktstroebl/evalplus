

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
    if not 1 <= base <= 10:
        raise ValueError(f"base has to be between 1 and 10, not {base}")
    if not isinstance(x, int) or x <= 0:
        raise ValueError(f"x has to be a positive integer, not {x}")

    div, mod = divmod(x, base)
    if div == 0:
        return str(mod)
    return change_base(div, base) + str(mod)

