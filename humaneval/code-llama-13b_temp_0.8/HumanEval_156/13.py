
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
    mini_roman = {1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l',
                  90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    roman_num = ""
    if number == 0:
        return None
    if number >= 1000:
        roman_num += mini_roman[1000]
        number -= 1000
    if number >= 500:
        roman_num += mini_roman[500]
        number -= 500
    if number >= 100:
        roman_num += mini_roman[100]
        number -= 100
    if number >= 50:
        roman_num += mini_roman[50]
        number -= 50
    if number >= 10:
        roman_num += mini_roman[10]
        number -= 10
    if number >= 5:
        roman_num += mini_roman[5]
        number -= 5
    if number >= 1:
        roman_num += mini_roman[1]
        number -= 1
    return roman_num.lower()

