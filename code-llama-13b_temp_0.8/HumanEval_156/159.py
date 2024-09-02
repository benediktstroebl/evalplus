
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

    numbers_to_romans = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix',
        10: 'x', 40: 'xl', 50: 'l', 90: 'xc',
        100: 'c', 400: 'cd', 500: 'd', 900: 'cm',
        1000: 'm', 4000: 'm', 5000: 'm', 9000: 'm'
    }

    roman = ''
    roman_numeral_value = 0
    for value, roman_numeral in sorted(numbers_to_romans.items(), reverse=True):
        while number >= value:
            number -= value
            roman += roman_numeral
            roman_numeral_value += value
    return roman

