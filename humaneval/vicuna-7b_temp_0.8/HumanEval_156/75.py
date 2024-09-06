
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
    roman_map = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    roman_map.update({
        200: 'II',
        100: 'I',
        50: 'V',
        40: 'IV',
        30: 'III',
        20: 'II',
        10: 'I',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
        250: 'XXV',
        200: 'XX',
        100: 'X',
        50: 'V',
        40: 'IV',
        30: 'III',
        20: 'II',
        10: 'I',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    })

    roman_numeral = ''
    while number > 0:
        digit = number % 10
        number //= 10
        roman_numeral += roman_map[digit]

    return roman_numeral.lower()
