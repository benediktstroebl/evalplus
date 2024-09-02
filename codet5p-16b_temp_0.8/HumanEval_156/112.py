
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

    dictionary = {
        1:'i',
        5:'v',
        10:'x',
        50:'l',
        100:'c',
        500:'d',
        1000:'m'
    }

    return ''.join([dictionary[i] for i in dictionary if i <= number])
