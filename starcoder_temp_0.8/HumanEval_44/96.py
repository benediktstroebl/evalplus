

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
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Please enter integers!")
    if x == 0:
        return "0"
    if x < 0:
        return "-" + change_base(-x, base)
    return (change_base(x // base, base) +
            change_base(x % base, base))

