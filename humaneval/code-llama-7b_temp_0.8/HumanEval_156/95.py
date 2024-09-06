
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
    if number < 1:
        raise ValueError('Invalid number')
    elif number > 1000:
        raise ValueError('Invalid number')

    roman_numbers = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }

    int_to_roman_map = {
        1: 1000,
        4: 100,
        5: 10,
        9: 1000,
        10: 100,
        40: 10,
    }

    roman_string = ''
    while number > 0:
        for num, roman in roman_numbers.items():
            while number >= num:
                roman_string += roman
                number -= num

    for integer, roman in int_to_roman_map.items():
        roman_string = roman_string.replace(roman, '{}'.format(roman) * integer)

    return roman_string.lower()

