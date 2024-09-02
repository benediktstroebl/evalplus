
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
        6: 'VI',
        9: 'IX',
        4: 'IV',
        1: 'I'
    })  # 69 -> VIX, 70 -> VII
    roman_map.update({
        4: 'IV',
        3: 'III',
        2: 'II',
        1: 'I'
    })  # 400 -> CD
    roman_map.update({
        9: 'X',
        5: 'V',
        4: 'IV',
        1: 'I'
    })  # 445 -> XLIV
    roman_map.update({
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    })  # 426 -> CDXXVI
    roman_map.update({
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
    })  # 19 -> xix
    result = []
    for i, n in enumerate(str(number)):
        result.append(roman_
