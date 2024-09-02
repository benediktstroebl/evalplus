
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
    if number == 0:
        return ''
    elif number <= 3:
        return 'i' * number
    elif number == 4:
        return 'iv'
    elif number <= 9:
        return 'v' + 'i' * (number - 5)
    elif number == 10:
        return 'x'
    elif number <= 30:
        return 'x' + 'i' * (number - 10)
    elif number == 40:
        return 'xl'
    elif number <= 90:
        return 'l' + 'x' * (number - 50)
    elif number == 100:
        return 'c'
    elif number <= 300:
        return 'c' + 'x' * (number - 100)
    elif number == 400:
        return 'cd'
    elif number <= 900:
        return 'd' + 'c' * (number - 500)
    elif number == 1000:
        return 'm
