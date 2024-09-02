
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
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = ''
    while number > 0:
        if number >= roman_dict['M']:
            number -= roman_dict['M']
            result += 'M'
        elif number >= roman_dict['D']:
            number -= roman_dict['D']
            result += 'D'
        elif number >= roman_dict['C']:
            number -= roman_dict['C']
            result += 'C'
        elif number >= roman_dict['L']:
            number -= roman_dict['L']
            result += 'L'
        elif number >= roman_dict['X']:
            number -= roman_dict['X']
            result += 'X'
        elif number >= roman_dict['V']:
            number -= roman_dict['V']
            result += 'V'
        elif number >= roman_dict['I']:
