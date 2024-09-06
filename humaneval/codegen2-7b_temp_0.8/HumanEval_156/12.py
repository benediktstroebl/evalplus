
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
    romans = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii']
    result = ''
    for i in range(number):
        result += romans[(number-1)/10**i % 10]
    return result
