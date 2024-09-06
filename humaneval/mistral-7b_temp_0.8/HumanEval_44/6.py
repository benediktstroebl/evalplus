

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
    base_list = list('1234567890')
    result = ''
    while x > 0:
        index = x % base
        result = base_list[index] + result
        x = x // base
    return result

