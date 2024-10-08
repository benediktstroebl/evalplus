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
    if number <= 100:
        return 'a' + number
    elif number >=  103 and number <= 150:
        return 'ce' + int_to_mini_roman(number - 100)
    elif number >= 151 and number <= 200:
        return 'd' + int_to_mini_roman(number - 150)
    elif number >= 201 and number <= 250:
        return 'c' + int_to_mini_roman(number - 200)
    elif number >= 251 and number <= 300:
        return 'b' + int_to_mini_roman(number - 250)
    elif number >= 301 and number <= 350:
        return 'a' + int_to_mini_roman(number - 300)
    elif number >= 351 and number <= 400:
        return 'd' + int_to_mini_roman(number - 350)
    elif number >= 401 and number <= 500:
        return 'c' + int_to_mini_roman(number - 400)
    elif number >= 501 and number <= 600:
        return 'b' + int_to_mini_roman(number - 450)
    elif number >= 601 and number <= 700:
        return 'a' + int_to_mini_roman(number - 600)
    elif number >= 701 and number <= 800:
        return 'd' + int_to_mini_roman(number - 700)
    elif number >= 801 and number <= 900:
        return 'c' + int_to_mini_roman(number - 800)
    else:
        return 'x' + int_to_mini_roman(number - 900)