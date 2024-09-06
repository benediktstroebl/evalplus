
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
    int_to_roman_dict = {
        1 : 'i',
        5 : 'v',
        10 : 'x',
        50 : 'l',
        100 : 'c',
        500 : 'd',
        1000 : 'm',
        }
    roman_dict_values = list(int_to_roman_dict.values())
    roman_dict_keys = list(int_to_roman_dict.keys())
    mini_roman_dict = {}
    for key, value in zip(roman_dict_keys, roman_dict_values):
        mini_roman_dict[key] = value
        mini_roman_dict[key*2] = value + value
        mini_roman_dict[key*3] = value + value + value
        mini_roman_dict[key*4] = value + 'iv'
        mini_roman_dict[key*5] = value + value + 'v'
        mini_roman_dict[key*9] = value + 'ix'
        mini_roman_dict[key*10] = value + 'x'
        mini_roman_dict[key*40] = value + 'xl'
        mini_roman_dict[key*50] = value + 'l'
        mini_roman_dict[key*90] = value + 'xc'
        mini_roman_dict[key*100] = value + 'c'
        mini_roman_dict[key*400] = value + 'cd'
        mini_roman_dict[key*500] = value + 'd'
        mini_roman_dict[key*900] = value + 'cm'
        mini_roman_dict[key*1000] = value + 'm'
    return ''.join([mini_roman_dict[number]]).lower()
