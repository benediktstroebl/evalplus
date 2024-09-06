

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
    if base <= 10:
        digit_list = []
        while x > 0:
            digit = x % base
            digit_list.append(digit)
            x = x // base
        digit_list.reverse()
        result = ''.join(map(str, digit_list))
        return result
    else:
        return 0
