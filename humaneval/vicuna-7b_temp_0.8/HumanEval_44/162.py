

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
        if x == 0:
            return '0'
        while x != 0 and x % base != 0:
            x //= base
            base -= 1
        return ''.join([str(x) for i in range(len(str(base)) - len(str(x)))])
    else:
        return x
