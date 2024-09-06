
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
    roman_numerals = {
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
        1000: 'm',
    }

    def build_string(number, string):
        if number == 0:
            return string
        if number in roman_numerals.keys():
            string += roman_numerals[number]
            return build_string(0, string)
        else:
            for i in range(len(roman_numerals.keys()), 0, -1):
                if number - i in roman_numerals.keys():
                    string += roman_numerals[i]
                    return build_string(number - i, string)

    return build_string(number, '').lower()
