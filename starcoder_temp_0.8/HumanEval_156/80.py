
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

    # Build a dictionary of the roman numerals
    numerals = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500:'d',
        1000:'m'
    }

    # Find the largest key that is less than or equal to num.
    # This will be the highest roman numeral in our answer
    largest_key = min([key for key in numerals.keys() if key <= number])

    # Build up a list of roman numerals
    roman_numeral = []
    while number > 0:
        # Find the next largest roman numeral
        roman_numeral.append(numerals[largest_key])
        # Subtract it out from the number we need to convert
        number -= largest_key
        # Find the next largest roman numeral
        largest_key = min([key for key in numerals.keys() if key <= number])

    # Return the roman numeral as a single string.
    return ''.join(roman_numeral)
