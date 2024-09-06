
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
    roman_dict = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
    roman_key_list = list(roman_dict.keys())
    roman_value_list = list(roman_dict.values())

    roman_val = ''

    for i in range(len(roman_key_list)):
        if number >= roman_key_list[i]:
            roman_val += roman_value_list[i] * (number // roman_key_list[i])
            number %= roman_key_list[i]

    return roman_val

