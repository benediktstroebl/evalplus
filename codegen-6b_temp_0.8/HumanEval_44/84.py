

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
    letter = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if x < 0:  # change base for negative input number
        return change_base(-x, base)
    if x == 0:  # 0 is represented as "0" in string
        return ""
    if x % base == 0:  # if input number x is already in current base
        return str(x)
    cur_base = 1  # current base
    if x < base:  # if input number x is less than current base
        while x / cur_base != 0:
            cur_base *= base
        return str(x / cur_base) + letter[x % cur_base]
    if x >= base:  # if input number x is greater than current base
        return change_base(x - base, base) + letter[x % base]

