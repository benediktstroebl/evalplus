
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

    if number <= 0 or number > 1000:
        return ''

    mini_roman = ''
    while number > 0:
        if number - 1000 >= 0:
            mini_roman += 'm'
            number -= 1000
        elif number - 900 >= 0:
            mini_roman += 'cm'
            number -= 900
        elif number - 500 >= 0:
            mini_roman += 'd'
            number -= 500
        elif number - 400 >= 0:
            mini_roman += 'cd'
            number -= 400
        elif number - 100 >= 0:
            mini_roman += 'c'
            number -= 100
        elif number - 90 >= 0:
            mini_roman += 'xc'
            number -= 90
        elif number - 50 >= 0:
            mini_roman += 'l'
            number -= 50
        elif number - 40 >= 0:
            mini_roman += 'xl'
            number -= 40
        elif number - 10 >= 0:
            mini_roman += 'x'
            number -= 10
        elif number - 9 >= 0:
            mini_roman += 'ix'
            number -= 9
        elif number - 5 >= 0:
            mini_roman += 'v'
            number -= 5
        elif number - 4 >= 0:
            mini_roman += 'iv'
            number -= 4
        elif number - 1 >= 0:
            mini_roman += 'i'
            number -= 1
        else:
            mini_roman += '?'

    return mini_roman.lower()

