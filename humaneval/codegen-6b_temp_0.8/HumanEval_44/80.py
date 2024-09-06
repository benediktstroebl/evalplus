

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
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x < 0:
        return change_base(-x, base)
    if x == 0:
        return digits[0]
    if x > 0:
        return change_base(x//base, base) + digits[x % base]

