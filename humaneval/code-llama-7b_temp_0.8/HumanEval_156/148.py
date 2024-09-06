
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
    res = ''
    while number > 0:
        if number >= 1000:
            res += 'm'
            number -= 1000
        elif number >= 900:
            res += 'cm'
            number -= 900
        elif number >= 500:
            res += 'd'
            number -= 500
        elif number >= 400:
            res += 'cd'
            number -= 400
        elif number >= 100:
            res += 'c'
            number -= 100
        elif number >= 90:
            res += 'xc'
            number -= 90
        elif number >= 50:
            res += 'l'
            number -= 50
        elif number >= 40:
            res += 'xl'
            number -= 40
        elif number >= 10:
            res += 'x'
            number -= 10
        elif number >= 9:
            res += 'ix'
            number -= 9
        elif number >= 5:
            res += 'v'
            number -= 5
        elif number >= 4:
            res += 'iv'
            number -= 4
        elif number >= 1:
            res += 'i'
            number -= 1
    return res

