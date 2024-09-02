

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
        return '0'
    elif base == 1:
        return '1'
    else:
        x_str = str(x)
        base_str = str(base)
        if base_str == '1':
            return x_str[1:]
        else:
            result = x_str[0]
            for i in range(1, len(x_str)):
                result = result + str(int(x_str[i:i+1]) * (base_str[0]-1))
            return result