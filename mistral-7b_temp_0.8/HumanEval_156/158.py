
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
    roman_dict = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }
    roman_list = [
        'iv',
        'ix',
        'xv',
        'lx',
        'xc',
        'cd',
        'cm',
    ]

    if number > 1000:
        return 'invalid input'

    if number < 5:
        return roman_dict[number]

    if number == 5:
        return 'v'

    if number == 10:
        return 'x'

    if number == 15:
        return 'xv'

    if number == 20:
        return 'xx'

    if number == 25:
        return 'xv'

    if number == 50:
        return 'l'

    if number == 6
