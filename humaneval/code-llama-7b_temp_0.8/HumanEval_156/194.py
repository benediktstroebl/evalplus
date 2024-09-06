
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
    if number < 1 or number > 1000:
        raise ValueError('number must be between 1 and 1000')
    elif number <= 3:
        return 'iii'[0:number]
    elif number <= 5:
        return 'iv'[4 - number]
    elif number <= 8:
        return 'viii'[6 - number]
    elif number <= 10:
        return 'x'
    elif number <= 40:
        return 'x' + 'iv'[4 - (number - 5)]
    elif number <= 50:
        return 'l'
    elif number <= 90:
        return 'l' + 'ix'[6 - (number - 50)]
    elif number <= 100:
        return 'c'
    elif number <= 400:
        return 'c' + 'xl'[4 - (number - 100)]
    elif number <= 500:
        return 'd'
    elif number <= 900:
        return 'd' + 'cm'[4 - (number - 500)]
    else:
        return 'm'
