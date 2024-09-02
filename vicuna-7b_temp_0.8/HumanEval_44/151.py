

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
    result = ''
    for i in range(len(str(x))):
        digit = str(x)[i]
        value = x // (10**(len(str(base)) - 1 - i))
        for j in range(len(str(base)) - 1, -1, -1):
            if base[j] == digit:
                break
        else:
            value = 0
        result = str(base[i]) + result[j:]
        x = value * (10**(len(str(base)) - i - 1))
    return result