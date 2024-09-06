
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

    mini_roman = ''

    while number > 0:
        if number >= 1000:
            mini_roman += 'm'
            number -= 1000

        elif number >= 900:
            mini_roman += 'cm'
            number -= 900

        elif number >= 500:
            mini_roman += 'd'
            number -= 500

        elif number >= 400:
            mini_roman += 'cd'
            number -= 400

        elif number >= 100:
            mini_roman += 'c'
            number -= 100

        elif number >= 90:
            mini_roman += 'xc'
            number -= 90

        elif number >= 50:
            mini_roman += 'l'
            number -= 50

        elif number >= 40:
            mini_roman += 'xl'
            number -= 40

        elif number >= 10:
            mini_roman += 'x'
            number -= 10

        elif number >= 9:
            mini_roman += 'ix'
            number -= 9

        elif number >= 5:
            mini_roman += 'v'
            number -= 5

        elif number >= 4:
            mini_roman += 'iv'
            number -= 4

        elif number >= 1:
            mini_roman += 'i'
            number -= 1

    return mini_roman.lower()

