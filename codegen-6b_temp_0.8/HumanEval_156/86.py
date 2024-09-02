
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
    if not isinstance(number, int):
        raise TypeError("number {} is not a valid integer".format(number))
    if not is_valid_num(number):
        raise ValueError("number {} is not a valid integer".format(number))

    converter = Converter()
    if number > 1000:
        raise ValueError("number {} is too large".format(number))

    return converter.int_to_roman(number)

