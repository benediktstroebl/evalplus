
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
    roman_value = (
        (1000, 'm'), (500, 'd'), (100, 'c'), (50, 'l'),
        (10, 'x'), (5, 'v'), (1, 'i')
    )
    return ''.join(
        roman_value[i][1] * (number // roman_value[i][0])
        for i in range(len(roman_value))
    )

