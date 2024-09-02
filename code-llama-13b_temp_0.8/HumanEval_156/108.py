
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
    if number < 0 or number > 1000:
        raise ValueError
    result = ''
    while number >= 1000:
        number -= 1000
        result += 'm'
    while number >= 900:
        number -= 900
        result += 'cm'
    while number >= 500:
        number -= 500
        result += 'd'
    while number >= 400:
        number -= 400
        result += 'cd'
    while number >= 100:
        number -= 100
        result += 'c'
    while number >= 90:
        number -= 90
        result += 'xc'
    while number >= 50:
        number -= 50
        result += 'l'
    while number >= 40:
        number -= 40
        result += 'xl'
    while number >= 10:
        number -= 10
        result += 'x'
    while number >= 9:
        number -= 9
        result += 'ix'
    while number >= 5:
        number -= 5
        result += 'v'
    while number >= 4:
        number -= 4
        result += 'iv'
    while number >= 1:
        number -= 1
        result += 'i'
    return result

