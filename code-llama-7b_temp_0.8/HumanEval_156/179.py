
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
    # Find the roman numerals for the numbers below 1000, and
    # remember them in a dictionary.
    value_to_numeral_map = {
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

    roman_numeral = ''
    for value in value_to_numeral_map:
        # Remove all the multiples of the current value from the number.
        number %= value
        # Then, append the appropriate numeral to the answer.
        roman_numeral += value_to_numeral_map[value] * (number // value)
        # Finally, remove all the copies of the current value we just
        # appended to the answer.
        number //= value
    return roman_numeral.lower()

