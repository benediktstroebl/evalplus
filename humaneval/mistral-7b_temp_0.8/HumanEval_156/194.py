
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
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M',
    }

    def get_roman_representation(number, current_roman, place_value):
        if number > 0:
            current_roman.append(roman[place_value])
            return get_roman_representation(number - place_value, current_roman, place_value)
        else:
            return current_roman

    roman_numeral = get_roman_representation(
        number, [],
        {1000: 1, 100: 2, 10: 3, 1: 4})

    return
