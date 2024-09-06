

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
    tens = base - 10
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    # base numbers are less than 10
    if base < 10:
        if x == 0:
            return '0'
        elif x < 0:
            return '-' + change_base(-x, base)
        elif x == 10:
            return 'A'
        else:
            return change_base(x, base)

    # base numbers are 10
    if x == 0:
        return '0'
    elif x < 0:
        return '-' + change_base(-x, 10)
    else:
        return change_base_helper(x, base, 1, [])

