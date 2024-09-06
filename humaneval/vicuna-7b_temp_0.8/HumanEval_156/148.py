
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
    roman = ""
    if number < 1000:
        roman = str(number)[2:].upper()
    elif number < 10000:
        roman = "M" + str(number / 1000) + str(number % 1000)[2:]
    elif number < 100000:
        roman = "CM" + str(number / 10000) + str(number % 10000)[2:]
    elif number < 1000000:
        roman = "CD" + str(number / 100000) + str(number % 100000)[2:]
    elif number < 10000000:
        roman = "D" + str(number / 1000000) + str(number % 1000000)[2:]
    elif number < 1000000000:
        roman = "C" + str(number / 100000000) + str(number % 100000000)[2:]
    elif number < 10000000000000:
        roman = "L" + str(number / 10000000000000) + str(number % 10000000000000)[2:]
    elif number < 10000000000000000000:
        roman = "XC" + str(number / 1000000000000000000) + str(number % 1000000000000000000)[2:]
    else:
        roman = "CDL" + str(number / 1000000000000000000) + str(number % 1000000000000000000)[2:]
    return roman[2:-2].
