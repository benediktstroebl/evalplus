
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

    num = number
    mini_roman = ''
    roman_dict = {1000:'m',
                  900: 'cm',
                  500: 'd',
                  400: 'cd',
                  100: 'c',
                  90: 'xc',
                  50: 'l',
                  40: 'xl',
                  10: 'x',
                  9: 'ix',
                  5: 'v',
                  4: 'iv',
                  1: 'i'}

    while num > 0:
        for val in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            if num >= val:
                num -= val
                mini_roman += roman_dict[val]

    return mini_roman.lower()
