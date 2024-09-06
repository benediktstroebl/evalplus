
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

    dict_ = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000:'m',
    }

    result = ''

    while number:
        if number >= 1000:
            result += dict_[1000]
            number -= 1000
        elif number >= 500:
            result += dict_[500]
            number -= 500
        elif number >= 100:
            result += dict_[100] * (number // 100)
            number -= 100 * (number // 100)
        elif number >= 50:
            result += dict_[50] * (number // 50)
            number -= 50 * (number // 50)
        elif number >= 10:
            result += dict_[10] * (number // 10)
            number -= 10 * (number // 10)
        elif number >= 5:
            result += dict_[5] * (number // 5)
            number -= 5 * (number // 5)
        elif number >= 1:
            
