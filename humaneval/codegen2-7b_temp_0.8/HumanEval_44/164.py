

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
    x = str(x)
    if base < 2 or base > 10:
        raise ValueError("invalid base")
    if len(x) == 0:
        return "0"
    x = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[base**2:] + x
    return "".join(map(str, x))[:len(x
