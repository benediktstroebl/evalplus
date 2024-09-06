
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
    # write your code here

    roman_numeral = {}
    roman_numeral[1] = 'i'
    roman_numeral[4] = 'iv'
    roman_numeral[5] = 'v'
    roman_numeral[9] = 'ix'
    roman_numeral[10] = 'x'
    roman_numeral[40] = 'xl'
    roman_numeral[50] = 'l'
    roman_numeral[90] = 'xc'
    roman_numeral[100] = 'c'
    roman_numeral[400] = 'cd'
    roman_numeral[500] = 'd'
    roman_numeral[900] = 'cm'
    roman_numeral[1000] = 'm'

    if number == 0:
        return '0'

    number_of_digits = len(str(number))
    power = 10 ** (number_of_digits - 1)

    roman_string =
