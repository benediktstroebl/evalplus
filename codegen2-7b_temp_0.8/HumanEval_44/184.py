

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
    if x < base:
        return f"{base}"[x]
    elif x >= base and x < 10**(base+1):
        return f"{x - base}"[1]
    elif x >= 10**(base+1):
        return change_base(x // base**(base-1), base) + f"{x % base**(base-1)}"[1]
    else:
