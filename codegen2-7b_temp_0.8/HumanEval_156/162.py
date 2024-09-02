
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
    string_number = ''

    if number < 1 or number > 1000:
        raise ValueError('number has to be between 1 and 1000.')

    if number == 1000:
        string_number ='m'
    else:
        for num, word in enumerate(ROMAN_NUMS):
            while number >= word:
                string_number += word
                number -= word
    return string_number.lower
