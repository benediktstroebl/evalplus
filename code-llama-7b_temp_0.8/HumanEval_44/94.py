

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

    if x < 0:
        raise ValueError('Input x must be positive.')
    if base < 2:
        raise ValueError('Base must be greater than 1.')

    a = [int(i) for i in str(x)]
    k = len(a) - 1
    res = ''
    while k >= 0:
        res += str(a[k] * (base**k))
        k -= 1
    return res

