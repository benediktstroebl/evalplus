

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
    num = str(x)
    i = 0
    while i < len(num) and num[i] < base:
        i += 1
    while i < len(num) and num[i] >= base:
        num = "0" + num[i:]
        i += len(num)
    return num[:i].rjust(len(num), '0')
