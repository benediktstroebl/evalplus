

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

    if base < 2 or base > 36:
        return 'Invalid base'
    else:
        result = ''
        n = x
        while n > 0:
            n, i = divmod(n, base)
            result = str(i) + result
        return result

