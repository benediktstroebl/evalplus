
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
    if number <= 0:
        raise ValueError('Expected a positive integer')

    if number <= 999:
        return dict(zip(range(1, 100), ['ix', 'xv', 'xl', 'xc', 'xc', 'c','m']))[number]

