
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

    arabic_numbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    roman_numbers = {
        'I': 'i',
        'V': 'v',
        'X': 'x',
        'L': 'l',
        'C': 'c',
        'D': 'd',
        'M': 'm'
    }

    roman_numerals = ''

    for letter in number:
        if number[0] == 'I' and number[1] == 'V':
            roman_numerals = roman_numbers[letter] + roman_numerals

        elif number[0] == 'I' and number[1] == 'X':
            roman_numerals = roman_numbers[letter] + roman_numerals

        elif number[0] == 'I' and number[
