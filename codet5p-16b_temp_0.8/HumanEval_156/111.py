
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

    ret = ""
    while number!= 0:
        if number >= 1000:
            number -= 1000
            ret +='m'
        elif number >= 900:
            number -= 900
            ret += 'cm'
        elif number >= 500:
            number -= 500
            ret += 'd'
        elif number >= 400:
            number -= 400
            ret += 'cd'
        elif number >= 100:
            number -= 100
            ret += 'c'
        elif number >= 90:
            number -= 90
            ret += 'xc'
        elif number >= 50:
            number -= 50
            ret += 'l'
        elif number >= 40:
            number -= 40
            ret += 'xl'
        elif number >= 10:
            number -= 10
            ret += 'x'
        elif number >= 9:
            number -= 9
            ret += 'ix'
        elif number >= 5:
            number -= 5
            ret += 'v'
        elif number >= 4:
            number -= 4
            ret += 'iv'
        elif number
