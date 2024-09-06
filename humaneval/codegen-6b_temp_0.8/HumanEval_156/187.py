
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
    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError('Integers 1 to 1000 only please.')
    roman_number = ''
    while number > 0:
        if number >= 1000:
            roman_number += 'M'
            number -= 1000
        elif number >= 900:
            roman_number += 'CM'
            number -= 900
        elif number >= 500:
            roman_number += 'D'
            number -= 500
        elif number >= 400:
            roman_number += 'CD'
            number -= 400
        elif number >= 100:
            roman_number += 'C'
            number -= 100
        elif number >= 90:
            roman_number += 'XC'
            number -= 90
        elif number >= 50:
            roman_number += 'L'
            number -= 50
        elif number >= 40:
            roman_number += 'XL'
            number -= 40
        elif number >= 10:
            roman_number += 'X'
            number -= 10
        elif number >= 9:
            roman_number += 'IX'
            number -= 9
        elif number >= 5:
            roman_number += 'V'
            number -= 5
        elif number >= 4:
            roman_number += 'IV'
            number -= 4
        elif number >= 1:
            roman_number += 'I'
            number -= 1
    return roman_number.lower()

