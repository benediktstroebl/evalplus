
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
    int_to_roman = lambda number: {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }[number]

    roman_to_int = lambda roman: {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000,
    }[roman]

    number = int(number)
    if not 1 <= number <= 1000:
        raise ValueError("Number must be between 1 and 1000")

    if number == 0:
        return ''

    roman_number = ''

    for decimal_place, number in enumerate(reversed(str(number)), 1):
        number = int(number)
        if number == 4:
            roman_number += int_to_roman(5 ** decimal_place)
        elif number >= 5:
            roman_number += int_to_roman(5 ** decimal_place) + int_to_roman(number - 5 ** decimal_place)
        else:
            roman_number += int_to_roman(number)

    return roman_number.lower()
