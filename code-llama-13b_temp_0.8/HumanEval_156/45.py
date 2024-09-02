
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
    # The mapping from integers to roman numerals
    roman_numerals = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix',
        10: 'x', 40: 'xl', 50: 'l', 90: 'xc',
        100: 'c', 400: 'cd', 500: 'd', 900: 'cm',
        1000: 'm'
    }
    # Add the "0" key to the mapping.
    roman_numerals[0] = ''

    def mini_roman(number):
        """
        Given a positive integer, obtain its roman numeral equivalent as a
        string, and return it in lowercase.
        """
        mini_roman = ''
        for integer, roman in sorted(roman_numerals.items(), reverse=True):
            # Apply the mapping
            mini_roman += roman * (number // integer)
            # We do integer -= integer so that integer gets smaller
            # each time, hence we are left with only one digit left over
            # in the end, and the for loop exits.
            number -= integer
        return mini_roman

    return mini_roman(number)
