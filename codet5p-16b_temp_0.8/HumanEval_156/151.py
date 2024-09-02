
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

    roman = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000:'m'
    }
    res = ''
    while number:
        if number >= 1000:
            number -= 1000
            res += roman[1000]
        elif number >= 500:
            number -= 500
            res += roman[500]
        elif number >= 100:
            number -= 100
            res += roman[100]
        elif number >= 50:
            number -= 50
            res += roman[50]
        elif number >= 10:
            number -= 10
            res += roman[10]
        elif number >= 5:
            number -= 5
            res += roman[5]
        elif number >= 1:
            number -= 1
            res += roman[1]
    return res
