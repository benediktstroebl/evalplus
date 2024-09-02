
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
    return roman_converter(number,
                           number_to_roman={1: 'i', 4: 'iv', 5: 'v', 9: 'ix'},
                           number_to_roman_dict={10: 'x', 40: 'xl', 50: 'l', 90: 'xc'},
                           number_to_roman_dict_100={100: 'c', 400: 'cd', 500: 'd', 900: 'cm'},
                           number_to_roman_dict_1000={1000: 'm'})

