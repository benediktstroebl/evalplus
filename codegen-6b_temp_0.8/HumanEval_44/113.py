

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
    lst = []
    while x:
        lst.append(int(x % base))
        x //= base
    lst.reverse()
    lst = [str(x) for x in lst]
    return "".join(lst)

