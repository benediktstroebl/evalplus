
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

    mini_roman = ''
    # The integers are the same as the roman numerals, but
    # in descending order
    mini_roman_numerals = ('m', 'd', 'c', 'l', 'x', 'v', 'i')
    mini_roman_values = (1000, 500, 100, 50, 10, 5, 1)
    for i, value in enumerate(mini_roman_values):
        while number >= value:
            mini_roman += mini_roman_numerals[i]
            number -= value

    return mini_roman

