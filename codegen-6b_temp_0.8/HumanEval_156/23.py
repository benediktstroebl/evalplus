
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
    # TODO: Make this use a map to speed up
    if number < 1 or number > 1000:
        raise ValueError("Number out of range")

    if number < 100:
        return _int_to_mini_roman_helper(number)
    elif number == 100:
        return 'c'
    elif number < 1000:
        return _int_to_mini_roman_helper(number % 100) + 'c'
    else:
        return _int_to_mini_roman_helper((number - 1000) % 100) + 'cd'

