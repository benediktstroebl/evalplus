
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
    roman_numeral = ''

    if number >= 1000:
        roman_numeral += 'M'

    if number >= 900:
        roman_numeral += 'CM'
        if number >= 1000:
            number -= 1000
            roman_numeral += 'D'
        else:
            roman_numeral += 'CD'
    elif number >= 800:
        roman_numeral += 'D'
        if number >= 900:
            number -= 900
            roman_numeral += 'C'
        else:
            roman_numeral += 'XC'
    elif number >= 700:
        roman_numeral += 'C'
        if number >= 800:
            number -= 800
            roman_numeral += 'L'
        else:
            roman_numeral += 'XL'
    elif number >= 600:
        roman_numeral += 'L'
        if number >= 700:
            number -= 700
            roman_numeral += 'XC'
        else:
            roman_numeral += 'IX'
    elif number >= 500:
        roman_numeral += 'XC'
        if number >= 600:
            number -= 600
            roman_numeral += 'L'
        else:
            roman_numeral += 'XL'
    elif number >= 400:
        roman_numeral += 'XL'
        if number >= 500:
            number -= 500
            roman_numeral += 'L'
        else:
            roman_numeral += 'XLI'
    elif number >= 300:
        roman_numeral += 'LI'
        if number >= 400:
            number -= 400
            roman_numeral += 'L'
        else:
            roman_numeral += 'XLI'
    elif number >= 200:
        roman_numeral += 'XLI'
        if number >= 300:
            number -= 30
