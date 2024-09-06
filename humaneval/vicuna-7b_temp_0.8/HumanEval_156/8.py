
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
    numerators = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
    denominators = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    numerator = number // 1000
    denominator = number % 1000
    roman_numeral = ''
    while numerator >= 49:
        roman_numeral += numerators[numerator - 49]
        numerator -= 49
    while numerator >= 39:
        roman_numeral += numerators[numerator - 39]
        numerator -= 39
    while numerator >= 29:
        roman_numeral += numerators[numerator - 29]
        numerator -= 29
    while numerator >= 19:
        roman_numeral += numerators[numerator - 19]
        numerator -= 19
    numerator = number // 100
    denominator = number % 100
