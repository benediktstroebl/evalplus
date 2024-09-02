
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
    MAX = 1000
    ROMANS = { 1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
                100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
                 10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
                1: 'I' }
    roman_numeral = ''
    for roman_numeral_to_int, integer_part in ROMANS.items():
        while number >= roman_numeral_to_int:
            roman_numeral += integer_part
            number -= roman_numeral_to_int
    return roman_numeral.lower()
