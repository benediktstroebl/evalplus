
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
    if number < 1 or number > 1000:
        raise ValueError('int_to_mini_roman: number must be between 1 and 1000')
    roman_numeral = ''
    while number > 0:
        if number >= 1000:
            roman_numeral += 'M'
            number -= 1000
        elif number >= 900:
            roman_numeral += 'CM'
            number -= 900
        elif number >= 500:
            roman_numeral += 'D'
            number -= 500
        elif number >= 400:
            roman_numeral += 'CD'
            number -= 400
        elif number >= 100:
            roman_numeral += 'C'
            number -= 100
        elif number >= 90:
            roman_numeral += 'XC'
            number -= 90
        elif number >= 50:
            roman_numeral += 'L'
            number -= 50
        elif number >= 40:
            roman_numeral += 'XL'
            number -= 40
        elif number >= 10:
            roman_numeral += 'X'
            number -= 10
        elif number >= 9:
            roman_numeral += 'IX'
            number -= 9
        elif number >= 5:
            roman_numeral += 'V'
            number -= 5
        elif number >= 4:
            roman_numeral += 'IV'
            number -= 4
        elif number >= 1:
            roman_numeral += 'I'
            number -= 1

    return roman_numeral.lower()

