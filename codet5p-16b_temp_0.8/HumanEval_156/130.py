
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
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    values = []
    for i in range(3):
        values.append(roman_numerals[number[i]])
    for i in range(2):
        if values[i] < values[i + 1]:
            values[i] = -values[i]
    return ''.join([f'{roman_numerals[roman_numeral]}{roman_numerals[roman_numeral+1] * value}' for roman_numeral, value in zip('IIVXLCDM', values)])
