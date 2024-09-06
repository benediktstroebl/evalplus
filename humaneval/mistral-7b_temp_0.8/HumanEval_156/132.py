
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
    ROMAN_SYMBOLS = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}
    DIVIDERS = {1: 1, 5: 10, 10: 100, 50: 1000, 100: 10000, 500: 100000, 1000: 1000000}
    NUMBERS = {1: 1, 5: 5, 10: 10, 50: 50, 100: 100, 500: 500, 1000: 1000}
    DIVIDER_MULTIPLE = {1: 1, 5: 5, 10: 10, 50: 50, 100: 100, 
