
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
    result = ''
    temp = 0
    number = number % 1000
    while number > 0:
        if number // 1000 > 0:
            number -= number // 1000 * 1000
            result += roman_dict[1000]
        elif number // 100 >= 0:
            number -= number // 100 * 100
            result += roman_dict[100]
        elif number // 10 >= 0:
            number -= number // 10 * 10
            result += roman_dict[10]
        elif number // 5 >= 0:
            number -= number // 5 * 5
            result += roman_dict[5]
        else:
            number -= number // 1 * 1
            result
