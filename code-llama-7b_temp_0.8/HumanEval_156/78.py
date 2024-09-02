
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

    int_to_roman = {
        1 : 'i',
        5 : 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }

    numbers = []

    while number:
        if number >= 1000:
            number -= 1000
            numbers.append('m')
        elif number >= 900:
            number -= 900
            numbers.append('cm')
        elif number >= 500:
            number -= 500
            numbers.append('d')
        elif number >= 400:
            number -= 400
            numbers.append('cd')
        elif number >= 100:
            number -= 100
            numbers.append('c')
        elif number >= 90:
            number -= 90
            numbers.append('xc')
        elif number >= 50:
            number -= 50
            numbers.append('l')
        elif number >= 40:
            number -= 40
            numbers.append('xl')
        elif number >= 10:
            number -= 10
            numbers.append('x')
        elif number >= 9:
            number -= 9
            numbers.append('ix')
        elif number >= 5:
            number -= 5
            numbers.append('v')
        elif number >= 4:
            number -= 4
            numbers.append('iv')
        else:
            number -= 1
            numbers.append('i')

    return ''.join(numbers)
