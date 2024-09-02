
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

    roman = {1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000:'m'}
    num_div = [[1000,'m'], [900, 'cm'], [500, 'd'], [400, 'cd'], [100, 'c'], [90, 'xc'], [50, 'l'], [40, 'xl'], [10, 'x'], [9, 'ix'], [5, 'v'], [4, 'iv'], [1, 'i']]

    result = ""
    for i in num_div:
        while number >= i[0]:
            result += roman[i[0]]
            number -= i[0]
    return result
