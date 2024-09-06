

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
    if base == 0:
        return ''
    elif base % 10 == 0:
        return str(x)
    elif base == 10:
        return x
    elif base == 2:
        return '1' + str(x)
    elif base == 4:
        return str(x) + '4'
    elif base == 5:
        return str(x) + '5'
    elif base == 6:
        return str(x) + '6'
    elif base == 8:
        return str(x) + '8'
    else:
        if base % 10 == 1:
            return str(x * 10) + '1'
        elif base % 10 == 2:
            return str(x * 10) + '2'
        elif base % 10 == 3:
            return str(x * 10) + '3'
        elif base % 10 == 4:
            return str(x * 10) + '4'
        elif base % 10 == 5:
            return str(x * 10) + '5'
        elif base % 10 == 6:
            return str(x * 10) + '6'
        elif base % 10 == 7:
            return str(x * 10) + '7'
        elif base % 10 == 8:
            return str(x * 10) + '8'
        else:
            result = str(x)
            while base > 0:
                remainder = result % 10
                result = (remainder + 10) % base
                if base > 0:
                    result = (remainder + 10) % base
            return result
