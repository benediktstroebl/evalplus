
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
    roman_numeral = ''

    if number == 0:
        return 'I'

    while number > 0:
        if number == 1:
            roman_numeral += 'I'
        elif number == 4 and number != 0:
            roman_numeral += 'IV'
        elif number == 5 and number != 0:
            roman_numeral += 'V'
        elif number == 9 and number != 0:
            roman_numeral += 'IX'
        else:
            roman_numeral += str(number % 10)
            number /= 10

    return roman_numeral.lower()
