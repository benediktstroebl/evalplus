
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
    # Initialize a dictionary to translate numbers to roman numerals
    roman_dictionary = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
        5000: ' ',
        10000: ' ',
    }

    # Initialize a list to store the roman numerals
    roman_numerals = []

    # Initialize a variable to store the remainder
    remainder = number

    # We will use a while loop to continue dividing the number by 10 until we
    # get to 0.
    while remainder > 0:
        # For each divisor of 10, check if the remainder is larger than or equal
        # to the divisor. If so, append the roman numeral of the divisor to the
        # list. Then, set the remainder to the remainder minus the divisor.
        if remainder >= 1000:
            roman_numerals.append(roman_dictionary[1000])
            remainder -= 1000
        elif remainder >= 500:
            roman_numerals.append(roman_dictionary[500])
            remainder -= 500
        elif remainder >= 100:
            roman_numerals.append(roman_dictionary[100])
            remainder -= 100
        elif remainder >= 50:
            roman_numerals.append(roman_dictionary[50])
            remainder -= 50
        elif remainder >= 10:
            roman_numerals.append(roman_dictionary[10])
            remainder -= 10
        elif remainder >= 5:
            roman_numerals.append(roman_dictionary[5])
            remainder -= 5
        else:
            roman_numerals.append(roman_dictionary[1])
            remainder -= 1

    return ''.join(roman_numerals)

