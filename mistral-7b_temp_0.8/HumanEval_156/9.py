
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    symbol = 'ivxlcdm'
    power = [1, 5, 10, 50, 100, 500, 1000]
    result = []
    for p, s in zip(power, symbol):
        num = number // p
        if num:
            number -= num * p
            result.append([num, s])
    if len(result) == 0:
        return ''
    else:
        return ''.join(str(n) + s for n, s in result)
