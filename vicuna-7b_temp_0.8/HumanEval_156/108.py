
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
    roman = ''
    while number >= 1000:
        roman += 'M'
        number -= 1000
    while number >= 500:
        roman += 'CM'
        number -= 500
    while number >= 100:
        roman += 'D'
        number -= 100
    while number > 0:
        roman += str(number)[-2:]
        number = number / 100
    return roman[::-1]
