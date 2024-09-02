
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
    # The simplest way to do this is to create a dictionary mapping
    # integers to their roman numeral equivalents.
    conversions = {1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c',
                   90: 'xc', 50: 'l', 40: 'xl', 10: 'x', 9: 'ix', 5: 'v',
                   4: 'iv', 1: 'i'}

    # Then just find the number of times each digit appears in the integer.
    # This can be done by using a dictionary comprehension.
    digit_counts = {key: (number // key) for key in conversions}

    # Then the digits in roman numerals are obtained by multiplying the
    # digit count by the digit's roman numeral value.
    roman_numeral = ''
    for key in conversions:
        roman_numeral += digit_counts[key] * conversions[key]

    return roman_numeral.lower()
