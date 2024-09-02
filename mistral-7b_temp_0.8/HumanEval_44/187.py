

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

    if base > 10:
        raise ValueError('base must be less than 10')

    if x == 0:
        return '0'

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if base == 10:
        return str(x)

    result = ''
    while x != 0:
        i = x % base
        x = x // base
        result = numbers[i] + result
    return result

