
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
    if number == 0:
        return 'null'
    elif number < 0:
        raise ValueError('must be a positive number')
    elif number < 1000:
        return _mini_to_roman[number]
    elif number == 1000:
        return'm'
    else:
        raise ValueError('must be between 1 and 1000 inclusive
