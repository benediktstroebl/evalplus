

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
    x = bin(x)[2:]
    x = x.zfill(len(x) + 8)
    x = x.replace('0b', '')
    x = x.replace('0o', '')
    x = x.replace('0', '')
    x = x.strip()
    x = int(x, base)
    return bin(x
