

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
        return -1 * change_base(-1 * x, base)
    if x < 10:
        return str(x)
    last_digit = x % base
    if last_digit == 10:
        return "A"
    elif last_digit == 11:
        return "B"
    elif last_digit == 12:
        return "C"
    elif last_digit == 13:
        return "D"
    elif last_digit == 14:
        return "E"
    elif last_digit == 15:
        return "F"
    else:
        return change_base(x // base, base) + str(last_digit)
