

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
    d = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j',
         20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't',
         30: 'u', 31: 'v', 32: 'w', 33: 'x', 34: 'y', 35: 'z'}
    if base > 35:
        return change_base(
            x, base % 35) + change_base(
            x // 35, 35) if x > 35 else str(x % 35)
    if x < 10:
        return str(x)
    else:
        return change_base(
            x // base, base) + d[x % base] if x > 35 else str(x % base)

