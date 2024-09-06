

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
    x = x % base
    if x == 0:
        return "0"
    else:
        while x >= base:
            x = x // base
            if x == 0:
                break
        return "".join(chr(x) for x in range(base-1, 0, -1))
