
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
    if number >= 3000 or number <= 0:
        raise ValueError('number must be in range [1, 3000]')

    result = []
    references = [(1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'), (100, 'c'), (90, 'xc'), (50, 'l'), (40, 'xl'),
                  (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')]
    for reference in references:
        value, letters = reference
        count = number // value
        result += letters * count
        number %= value

    return ''.join(result).lower()

