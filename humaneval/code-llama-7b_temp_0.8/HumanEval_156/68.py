
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
    int_to_roman = {
        1 : 'i',
        5 : 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }

    roman_numeral = ''

    num_map = [(1000, 'm'), (500, 'd'), (100, 'c'), (50, 'l'), (10, 'x'), (5, 'v'), (1, 'i')]
    for num, roman in num_map:
        count, number = divmod(number, num)
        roman_numeral += count * roman

    return roman_numeral
