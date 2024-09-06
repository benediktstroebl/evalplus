

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

    result = []
    while x >= 1:
        temp = x % base
        if temp < 10:
            result.append(str(temp))
        else:
            result.append(chr(temp + ord('A') - 10))
        x = x // base
    result.reverse()
    return ''.join(result)

