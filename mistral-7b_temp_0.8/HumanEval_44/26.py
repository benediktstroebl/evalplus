

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
    if base < 10:
        x = int(x)
        if x < 0:
            raise ValueError('Negative number is not acceptable.')
        if x == 0:
            return '0'
        else:
            result = []
            while x > 0:
                mod = x % base
                result.append(str(mod))
                x = x // base
            result.reverse()
            return ''.join(result)
    else:
        raise ValueError('Base number must be less than 10.')

