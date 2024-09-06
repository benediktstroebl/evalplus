
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

    number = int(number)
    roman_dict = {
        1: 'x',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000:'m',
        1_000_000:'m',
        5_000_000: 'd',
        10_000_000: 'c',
        50_000_000: 'l',
        100_000_000: 'x',
        500_000_000: 'v',
        1_000_000_000:'m'
    }
    if number in roman_dict:
        return roman_dict[number]
    else:
        min_roman = ''
        while number!= 0:
            if number in [1, 10, 100, 1000]:
                roman_numeral = roman_dict[number]
                min_roman += roman_numeral
                number -= number
            elif number in [2, 3, 4]:
                roman_numeral = roman_dict[5 * number]
