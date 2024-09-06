
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
    if number < 1 or number > 1000:
        raise ValueError('Invalid integer')
    symbols = (('', '', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix'),
               ('', '', 'x', 'xx', 'xxx', 'XL', 'L', 'Lx', 'Lxx', 'Lxxx'),
               ('', '', 'c', 'cc', 'ccc', 'd', 'D', 'Dx', 'dx', 'Dxx'),
               ('', '', 'm', 'mm', 'mmc', 'M', 'm', 'mX', 'mXm', 'mXxx'))
    result = ''
    for symbol, small_numeral, large_numeral, thousands_numeral in symbols:
        if number >= 1000:
            result += thousands_numeral
            number -= 1000
        if number >= 900:
            result += large_numeral + symbols[3][2]
            number -= 900
        elif number >= 500:
            result += symbols[2][1]
            number -= 500
        elif number >= 400:
            result += symbols[2][0]
            number -= 400
        elif number >= 100:
            result += symbols[1][0]
            number -= 100
        elif number >= 90:
            result += symbols[1][2]
            number -= 90
        elif number >= 50:
            result += symbols[0][1]
            number -= 50
        elif number >= 40:
            result += symbols[0][0]
            number -= 40
        elif number >= 10:
            result += small_numeral
            number -= 10
        elif number >= 9:
            result += symbols[3][1]
            number -= 9
        elif number >= 5:
            result += symbols[3][0]
            number -= 5
        elif number >= 4:
            result += symbols[2][2]
            number -= 4
        elif number >= 1:
            result += symbols[2][3]
            number -= 1
    return result.lower()

