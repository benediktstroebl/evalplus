
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
    from collections import OrderedDict

    roman = {1: "i", 5: "v", 10: "x", 50: "l", 100: "c", 500: "d", 1000: "m"}
    roman_list = list(roman.keys())
    roman_list.sort()
    return "".join([roman[x] for x in range(1, number+1) if x in roman_list])

