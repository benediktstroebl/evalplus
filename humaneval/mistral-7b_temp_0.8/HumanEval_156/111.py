
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
    # TODO

    roman_map = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
    roman_numbers = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

    roman_num = ""
    while number != 0:
        if number >= 1000:
            roman_num += 'M'
            number -= 1000
        elif number >= 500:
            roman_num += 'D'
            number -= 500
        elif number >= 100:
            roman_num += 'C'
            number -= 100
        elif number >= 50:
            roman_num += 'L'
            number -= 50
        elif number >= 10:
            roman_num += 'X'
            number -= 10
        elif number >= 5:
            roman_num += 'V'
