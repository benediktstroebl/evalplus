
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
    if number < 0:
        return '-' + int_to_mini_roman(-number)
    if number < 20:
        return _int_to_mini_roman_dict[number]
    return _int_to_mini_roman_dict[20] + _int_to_mini_roman_dict[number % 10] + \
           _int_to_mini_roman_dict[number // 10
