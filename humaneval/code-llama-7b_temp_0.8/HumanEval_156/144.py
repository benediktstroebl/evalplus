
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
    if number == 0:
        return ''
    if number == 1:
        return 'i'
    if number == 2:
        return 'ii'
    if number == 3:
        return 'iii'
    if number == 5:
        return 'v'
    if number == 6:
        return 'vi'
    if number == 9:
        return 'ix'
    if number == 10:
        return 'x'
    if number == 40:
        return 'xl'
    if number == 50:
        return 'l'
    if number == 90:
        return 'xc'
    if number == 100:
        return 'c'
    if number == 400:
        return 'cd'
    if number == 500:
        return 'd'
    if number == 900:
        return 'cm'
    if number == 1000:
        return 'm'

    def int_to_roman(num):
        numerals = ((1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"))
        roman = ''
        for value, numeral in numerals:
            while num >= value:
                roman += numeral
                num -= value
        return roman

    return int_to_roman(number).lower()

