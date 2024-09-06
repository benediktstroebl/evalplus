
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
    conversion_table = {
        1000 : 'm',
        500 : 'd',
        100 : 'c',
        10 : 'x',
        1 : 'i'
    }
    return_string = ''
    for key in conversion_table:
        while number >= key:
            return_string += conversion_table[key]
            number -= key
    return return_string.lower()
