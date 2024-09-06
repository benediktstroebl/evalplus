
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
    roman_dict = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}
    if number in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        return roman_dict[number]
    elif number in (10, 11, 12, 13, 14, 15, 16, 17, 18, 19):
        return 'x' + roman_dict[number - 10]
    elif number in (50, 51, 52, 53, 54, 55, 56, 57, 58, 59):
        return 'l' + roman_dict[number - 50]
    elif number in (100, 101, 102, 103, 104, 105,
