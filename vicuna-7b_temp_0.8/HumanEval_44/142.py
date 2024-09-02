

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
    digits = [str(x) for x in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]
    result = ''
    for i in range(len(x)):
        result = ''.join([digits[x % d] for x in range(base)])
        if i < len(x) - 1:
            result = result[:-1]
            x %= base
    return result