

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
    new_base = list(str(x))
    new_base = new_base[::-1]
    new_base = [int(b) for b in new_base]
    res = []
    for index in range(len(new_base)):
        d, m = divmod(new_base[index], base)
        res.append(str(m))
    return ''.join(res[::-1])

