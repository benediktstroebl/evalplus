
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

    num_to_roman_dict = {
        1: 'i',
        4: 'ii',
        5: 'iii',
        9: 'iv',
        10: 'ix',
        40: 'x',
        50: 'x',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000:'m',
    }

    if number > 1000:
        raise ValueError("Input number is too large, should be less than or equal to 1000")

    if number in num_to_roman_dict:
        return num_to_roman_dict[number]

    reversed_dictionary = {v: k for k, v in num_to_roman_dict.items()}

    roman_numeral = ""

    while number:
        if number >= 1000:
            number -= 1000
            roman_numeral += reversed_dictionary[1000]
        elif number >= 900:
            number -= 900
            roman_numeral += reversed_dictionary[900]
        el
