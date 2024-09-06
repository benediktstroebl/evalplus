
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
    if not (1 <= number <= 1000):
        raise ValueError('Input number must be within 1 and 1000')
    elif number == 1:
        return 'i'
    elif number == 2:
        return 'ii'
    elif number == 3:
        return 'iii'
    elif number == 4:
        return 'iv'
    elif number == 5:
        return 'v'
    elif number == 6:
        return 'vi'
    else:
        return '
