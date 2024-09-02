
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
    5: 'v',
    10: 'x',
    50: 'l',
    100: 'c',
    500: 'd',
    1000: 'm'
    }
    if number == 1:
        return roman_numerals[1]
    roman_numeral_list = [roman_numerals[number]]
    while number // 5 != 0:
        if number >= 10:
            roman_numeral_list.append(roman_numerals[5])
            number = number - 5
        else:
            roman_numeral_list.append(roman_numerals[5])
            number = 0
    while number // 10 != 0:
        if number >= 100:
            roman_numeral_list.append(roman_numerals[10])
            number = number - 10
        else:
            roman_numeral_list.append(roman_numerals[10])
