

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
    if base < 2 or base > 9:
        return "No such base!"
    else:
        for i in range(2, base + 1):
            for j in range(2, base + 1):
                for k in range(2, base + 1):
                    if (i + j) == k:
                        return "No such base!"
    result = ''
    while x:
        n = x % base
        if n == 0:
            n = 10
        result = str(n) + result
        x = x // base
    return result
