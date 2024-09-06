
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
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_numerals = ['m', 'cm', 'd', 'cd', 'c', 'xc', 'l', 'xl', 'x', 'ix', 'v', 'iv', 'i']
    result = ''
    i = 0

    while number > 0:
        quotient = number // values[i]
        if quotient == 4:
            result += roman_numerals[i] + roman_numerals[i + 1]
        elif quotient == 9:
            result += roman_numerals[i] + roman_numerals[i + 2]
        else:
            result += quotient * roman_numerals[i]
        number %= values[i]
        i += 2
    return result.lower()

