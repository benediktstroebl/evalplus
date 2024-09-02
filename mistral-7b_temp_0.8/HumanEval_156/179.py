
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
    romans = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }
    roman_string = ''
    for roman, int_value in romans.items():
        if number >= int_value:
            roman_string += int(number // int_value) * int_value * romans.get(int_value)
            number -= int(number // int_value) * int_value
    return roman_string

