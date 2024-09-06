

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
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if x < 0:
        result_str = ''
    elif x == 0:
        result_str = '0'
    else:
        result = []
        while x > 0:
            result.append(str(x % base))
            x //= base
        result = result[::-1]
        result_str = ''.join(result)
    if result_str == '':
        return '0'
    else:
        return result_str
