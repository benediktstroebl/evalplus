
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
    # Initial dictionary of roman numerals.
    roman_numerals = {
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
        1: 'i'
    }

    # If number is not a positive integer, return false.
    if number <= 0 or not type(number) is int:
        return False

    # Create an empty string to store roman numerals.
    roman_number = ""

    # Loop through the roman_numerals dictionary until we hit 0.
    while number > 0:
        for key in roman_numerals:
            # Convert the key to a string and slice off the last digit.
            key_string = str(key)[-1]

            # If the last digit
