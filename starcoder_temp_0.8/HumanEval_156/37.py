
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
    while number >= 900:
        roman += 'CM'
        number -= 900
    while number >= 500:
        roman += 'D'
        number -= 500
    while number >= 400:
        roman += 'CD'
        number -= 400
    while number >= 100:
        roman += 'C'
        number -= 100
    while number >= 90:
        roman += 'XC'
        number -= 90
    while number >= 50:
        roman += 'L'
        number -= 50
    while number >= 40:
        roman += 'XL'
        number -= 40
    while number >= 10:
        roman += 'X'
        number -= 10
    while number >= 9:
        roman += 'IX'
        number -= 9
    while number >= 5:
        roman += 'V'
        number -= 5
    while number >= 4:
        roman += 'IV'
        number -= 4
    while number >= 1:
        roman += 'I'
        number -= 1
    return roman
