

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
    if x == 0:
        return '0'
    if x < 0:
        sign = '-'
        x = x * -1
    else:
        sign = ''
    x = abs(x)
    result = ''
    converted = {'0': '0', '1': '1', '2': '2', '3': '3',
                 '4': '4', '5': '5', '6': '6', '7': '7',
                 '8': '8', '9': '9', 'A': '10', 'B': '11',
                 'C': '12', 'D': '13', 'E': '14', 'F': '15'}
    while x > 0:
        remainder = x % base
        result = str(converted[remainder]) + result
        x = x // base

    if result == '':
        return '0'
    else:
        return sign + result
