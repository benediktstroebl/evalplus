
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
    if not isinstance(number, int):
        raise TypeError("Please pass a positive integer")
    if number < 0:
        raise ValueError("Please pass a positive integer")
    if number > 1000:
        raise ValueError("Please pass a number between 1 and 1000")
    if number < 1:
        raise ValueError("Please pass a positive integer")

    # basic 1-9 mapping
    roman_numerals_map = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }

    roman_numerals_map_reverse = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000,
    }

    # find the last significant digit
    number_digits = [int(i) for i in str(number)]
    significant_digit_index = len(number_digits) - 1
    # first convert the significant digit
    roman_numeral = roman_numerals_map[number_digits[significant_digit_index]]
    # now start from the penultimate digit
    for i in range(significant_digit_index - 1, -1, -1):
        significant_digit = number_digits[i]
        next_significant_digit = number_digits[i+1]
        # if the significant digit is less than the next significant digit
        # we need to find out if it can be replaced by two lesser digits
        if significant_digit < next_significant_digit:
            for key, value in roman_numerals_map.items():
                if key == next_significant_digit - significant_digit:
                    roman_numeral = value + roman_numeral
        # otherwise just append it
        else:
            roman_numer
