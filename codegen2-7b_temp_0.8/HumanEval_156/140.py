
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
    if not (isinstance(number, int) and number >= 0 and number <= 1000):
        raise Exception('Expected integer from 0 to 1000')

    roman = ''
    if number >= 9:
        roman +='m' * (number // 9)
        number %= 9
    if number >= 5:
        roman += 'd' * (number // 5)
        number %= 5
    if number >= 4:
        roman += 'c' * (number // 4)
        number %= 4
    return r
