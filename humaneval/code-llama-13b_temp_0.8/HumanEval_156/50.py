
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
    roman_numeral_dict = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }

    # Special case for 0
    if number == 0:
        return ''

    # Starting from the highest place value, grab the
    # corresponding digit from the number and find the
    # corresponding roman numeral.
    roman_numeral_str = ''
    for place_value, roman_numeral in sorted(roman_numeral_dict.items(), reverse=True):
        while number >= place_value:
            roman_numeral_str += roman_numeral
            number -= place_value

    return roman_numeral_str.lower()

