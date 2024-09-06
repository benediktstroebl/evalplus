
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
    assert 0 <= number <= 1000, 'number must be positive and in the range of (0,1000)'

    def to_mini(d):
        return ''.join([mini_roman_to_int[i] for i in d])

    mini_roman_to_int = {
        'i': 1,
        'v': 5,
        'x': 10
    }

    return to_mini(divmod(number, 10)) + to_mini(divmod(number, 100 - 10 * 10))
