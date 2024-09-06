
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
    if number == 1000: return 'm'
    roman_numeral = ''
    if number >= 500:
        roman_numeral += 'd'
        number -= 500
    if number >= 100:
        roman_numeral += 'c'
        number -= 100
    if number >= 50:
        roman_numeral += 'l'
        number -= 50
    if number >= 10:
        roman_numeral += 'x'
        number -= 10
    if number >= 5:
        roman_numeral += 'v'
        number -= 5
    if number >= 1:
        roman_numeral += 'i'
        number -= 1
    return roman_numeral
