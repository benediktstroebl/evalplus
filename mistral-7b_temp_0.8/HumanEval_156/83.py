
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
    roman_dict = {
    1: 'i',
    5: 'v',
    10: 'x',
    50: 'l',
    100: 'c',
    500: 'd',
    1000: 'm',
    }
    roman_dict_inv = {v: k for k, v in roman_dict.items()}
    roman = ''
    while number:
        while number >= roman_dict[1]:
            roman += roman_dict[1]
            number -= 1
        while number >= roman_dict[5]:
            roman += roman_dict[5]
            number -= 5
        while number >= roman_dict[10]:
            roman += roman_dict[10]
            number -= 10
        while number >= roman_dict[50]:
            roman += roman_dict[50]
            number -= 50
        while number >= roman_dict[100]:
            roman += roman_dict[100]
            number -= 100
        while number >= roman_dict[
