
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

    roman_number = str(number)

    numeral_parts = [int(numeral_part) for numeral_part in roman_number]

    roman_parts = []
    for i, numeral_part in enumerate(numeral_parts):
        roman_part = roman_map.get(str(numeral_part))
        if roman_part:
            roman_parts.append(roman_part)
        else:
            roman_parts.append('0' + str(numeral_part))

    return ' '.join(roman_parts).lower()

