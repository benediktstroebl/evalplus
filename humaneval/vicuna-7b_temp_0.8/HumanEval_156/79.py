
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
    if number == 100:
        roman += 'X'
    elif number == 90:
        roman += 'IX'
    elif number == 80:
        roman += 'VIII'
    elif number == 70:
        roman += 'VII'
    elif number == 60:
        roman += 'VI'
    elif number == 50:
        roman += 'V'
    elif number == 40:
        roman += 'IV'
    elif number == 30:
        roman += 'III'
    elif number == 20:
        roman += 'II'
    elif number == 10:
        roman += 'I'
    else:
        roman += '0'
    return roman.lower()
