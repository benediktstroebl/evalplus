

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
    if base < 2:
        return x
    if x == 0:
        return 0
    end = []
    while x > 1:
        remain = x % base
        end.append(remain)
        x = x // base
    end.append(x)
    return ''.join(map(str, end[::-1]))

