

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

    power = 0
    result = ''
    while x > base:
        x, rem = divmod(x, base)
        result += str(rem)
        power += 1
    result += str(x)
    for _ in range(power):
        result += '0'
    return result[::-1]

