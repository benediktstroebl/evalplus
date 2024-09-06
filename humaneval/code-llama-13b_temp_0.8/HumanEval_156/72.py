
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
    d = {
        1000: 'm',
        500: 'd',
        100: 'c',
        50: 'l',
        10: 'x',
        5: 'v',
        1: 'i',
    }
    output = ''
    for key in sorted(d.keys(), reverse=True):
        while number >= key:
            number -= key
            output += d[key]
    return output

