
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
    roman = []
    if number == 0:
        roman.append('I')
    elif number > 0 and number < 10:
        roman.append(str(number))
    elif number >= 100 and number < 200:
        roman.append('C')
    elif number >= 200 and number < 300:
        roman.append('CC')
    elif number >= 300 and number < 400:
        roman.append('CCC')
    elif number >= 400 and number < 500:
        roman.append('CD')
    elif number >= 500 and number < 600:
        roman.append('CCE')
    elif number >= 600 and number < 700:
        roman.append('D')
    elif number >= 700 and number < 800:
        roman.append('DC')
    elif number >= 800 and number < 900:
        roman.append('DD')
    elif number >= 900 and number < 1000:
        roman.append('XC')
    else:
        roman.append('X')
    return ''.join(roman)
