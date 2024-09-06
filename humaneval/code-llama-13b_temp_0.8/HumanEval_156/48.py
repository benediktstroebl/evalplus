
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

    roman_num_dict = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }

    if type(number) is not int or number < 1 or number > 1000:
        raise TypeError("Input must be an integer between 1 and 1000")

    result = ''

    while number != 0:
        for base in [1000, 500, 100, 50, 10, 5, 1]:
            if number - base >= 0:
                number -= base
                result += roman_num_dict[base]
                break

    return result.lower()

