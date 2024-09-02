
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
    if number < 1 or number > 1000:
        raise ValueError('number out of range')
    # integer to roman numeral dictionary
    int_roman_dict = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm'
    }
    # format the number and find the roman numeral equivalents
    for i in reversed(range(1, len(str(number)) + 1)):
        place_holder = int(10 ** i)
        if place_holder < number:
            roman_equiv = int(number // place_holder)
            number %= place_holder
            if roman_equiv in int_roman_dict.keys():
                int_roman_dict[place_holder] = int_roman_dict[roman_equiv] + int_roman_dict[place_holder]
    roman_string = ''
    for key in sorted(int_roman_dict.keys(), reverse=True):
        roman_string += int_roman_dict[key] * (number // key)
        number %= key
    return roman_string.lower()

