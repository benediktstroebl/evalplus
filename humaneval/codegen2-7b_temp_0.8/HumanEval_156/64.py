
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
    dict_num = {1: 'i', 5: 'v', 10: 'x'}
    roman_num = ''
    for key, value in dict_num.items():
        while number >= key:
            number -= key
            roman_num += value
    return roman_num

