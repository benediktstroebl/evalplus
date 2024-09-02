
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
    if number > 999 or number < 1:
        raise ValueError('Integer value should be in range 1 <= num <= 1000')

    numeral = ''

    if number >= 1000:
        numeral +='m'
        number -= 1000

    if number >= 900:
        numeral += 'c'
        number -= 900

    while number >= 500:
        numeral += 'd'
        number -= 500

    while number >= 400:
        numeral += 'c'
        number -= 400

    return num
