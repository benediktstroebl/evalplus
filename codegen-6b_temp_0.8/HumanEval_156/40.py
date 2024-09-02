
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
        raise TypeError('Number should be a positive integer, got {}'.format(type(number)))

    if not 0 < number <= 1000:
        raise ValueError('Number must be between 1 and 1000')

    result = []  # We will store the roman equivalents here
    for numeral, arabic in ARABIC_ROMAN:
        while number >= arabic:
            result.append(numeral)
            number -= arabic

    return ''.join(result)

