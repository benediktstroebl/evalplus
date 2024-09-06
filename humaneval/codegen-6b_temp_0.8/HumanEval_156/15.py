
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
    assert 1 <= number <= 1000
    result = []
    for key, value in MINI_ROMAN.items():
        while number >= key:
            result.append(value)
            number -= key
    return ''.join(result)


assert int_to_mini_roman(19) == 'xix'
