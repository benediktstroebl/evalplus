
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
    if number > 1000:
        raise ValueError('Number must be between 1 and 1000')

    if number < 1:
        raise ValueError('Number must be greater than 0')

    roman = []
    roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    for i in range(len(roman_dict)):
        if number >= roman_dict[list(roman_dict.keys())[i]]:
            number -= roman_dict[list(roman_dict.keys())[i]]
            roman.append(list(roman_dict.keys())[i])

    return ''.join(roman)

