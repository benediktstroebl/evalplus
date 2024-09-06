
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

    int_to_roman = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'XD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }

    roman_int = ''
    if number > 3999:
        raise ValueError('Argument must be between 1 and 3999.')
    elif number in int_to_roman:
        return int_to_roman[number]

    for int_number, roman_number in int_to_roman.items():
        while number >= int_number:
            roman_int += roman_number
            number -= int_number

    return roman_int.lower()
