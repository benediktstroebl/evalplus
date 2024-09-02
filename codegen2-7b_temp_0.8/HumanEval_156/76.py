
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
    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError('The parameter must be an integer between 1 and 1000.')
    if number < 10:
        return roman_map[number]
    elif number < 20:
        return roman_map[number - 10]
    elif number < 100:
        return roman_map[(number - 10) // 5] + roman_map[(number - 10) % 5]
    return roman_map[
