

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

    if base < 2:
        raise ValueError('Base number is invalid')

    elif base == 10:
        return str(x)

    elif base == 2:
        binary = f'{x:b}'
        return binary.replace('0b', '')

    # get the length of input number (in digit representation)
    len_x = len(str(x))
    # get the length of expected output number
    len_y = len_x - 1
    # iterate over digits and convert them
    result = ''
    for i in range(len_y, -1, -1):
        digit = (x // (base ** i)) % base
        result = str(digit) + result

    return result

