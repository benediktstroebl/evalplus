

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
    assert 0 <= x < 10**len(str(x)), "The input number is too large"
    base_digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    while x > 0:
        # print(result,x)
        result.append(base_digits[x % base])
        x = x // base
    return ''.join(result[::-1])

