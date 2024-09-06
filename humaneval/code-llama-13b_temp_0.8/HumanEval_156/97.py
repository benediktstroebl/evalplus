
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
        raise ValueError('Number must be greater than 0')
    if number > 1000:
        raise ValueError('Number must be less than or equal to 1000')

    mini_roman = ''

    if number >= 100:
        mini_roman += 'c' * (number // 100)
        number %= 100

    if number >= 50:
        mini_roman += 'l'
        number -= 50

    if number >= 40:
        mini_roman += 'x' * 2
        number -= 40

    if number >= 10:
        mini_roman += 'x'
        number -= 10

    if number >= 5:
        mini_roman += 'v'
        number -= 5

    mini_roman += 'i' * number

    return mini_roman

