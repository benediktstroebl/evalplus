
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

    dict_roman_numerals = {1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

    if not 1 <= number <= 1000:
        return ''

    roman_numeral = ''

    while number > 0:
        if number >= 1000:
            roman_numeral += dict_roman_numerals[1000]
            number -= 1000

        elif number >= 900:
            roman_numeral += dict_roman_numerals[900]
            number -= 900

        elif number >= 500:
            roman_numeral += dict_roman_numerals[500]
            number -= 500

        elif number >= 400:
            roman_numeral += dict_roman_numerals[400]
            number -= 400

        elif number >= 100:
            roman_numeral += dict_roman_numerals[100]
            number -= 100

