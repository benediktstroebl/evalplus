
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
    # for a given number
    # find the largest possible digit
    # subtract the largest possible digit from the number
    # repeat until number is 0
    roman_letters = {
        1000: 'm',
        900: 'cm',
        500: 'd',
        400: 'cd',
        100: 'c',
        90: 'xc',
        50: 'l',
        40: 'xl',
        10: 'x',
        9: 'ix',
        5: 'v',
        4: 'iv',
        1: 'i',
    }
    roman_number = ''
    while number > 0:
        # find the largest possible digit
        for digit in roman_letters:
            if number >= digit:
                roman_letter = roman_letters[digit]
                break
        # subtract the largest possible digit from the number
        number -= digit
        # add the roman letter to the number
        roman_number += roman_letter
    return roman_number.lower()

