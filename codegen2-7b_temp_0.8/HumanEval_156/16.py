
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
    ranks = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']
    return ''.join(ranks[i] * int(i) for i in str(number))

