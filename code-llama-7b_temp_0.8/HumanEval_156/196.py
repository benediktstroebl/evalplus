
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
    # Mine is incorrect.
    # feature_to_roman = {
    #     1: 'i',
    #     5: 'v',
    #     10: 'x',
    #     50: 'l',
    #     100: 'c',
    #     500: 'd',
    #     1000: 'm',
    # }
    #
    # def num_to_roman(num):
    #     if num == 0:
    #         return ''
    #     for feature in (1000, 500, 100, 50, 10, 5, 1):
    #         if num >= feature:
    #             return feature_to_roman[feature] + num_to_roman(num - feature)
    #
    # return num_to_roman(number)
    #
    # import re
    # roman = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}
    # num = int(number)
    # def _to_roman(n):
    #     if n < 0 or n > 3000:
    #         raise Exception("Number must be between 1 and 3000")
    #     if n >= 1000:
    #         return roman[1000] + _to_roman(n - 1000)
    #     if n >= 900:
    #         return roman[900] + _to_roman(n - 900)
    #     if n >= 500:
    #         return roman[500] + _to_roman(n - 500)
    #     if n >= 400:
    #         return roman[400] + _to_roman(n - 400)
    #     if n >= 100:
    #         return roman[100] + _
