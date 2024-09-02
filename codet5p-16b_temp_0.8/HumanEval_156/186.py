
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

    if 1 <= number <= 1000:
        return ''.join([int_to_mini_roman(n) for n in range(1, number+1)])
    else:
        raise ValueError('Numeral should be in range [1, 1000].')
