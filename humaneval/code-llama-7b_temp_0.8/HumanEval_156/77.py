
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
    # Intialize a dictionary to be used to store roman numerals
    roman_numerals = {1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl',
                      50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd',
                      900: 'cm', 1000: 'm'}

    # Get the quotient and remainder of the division
    quotient, remainder = divmod(number, 10)
    if quotient >= 1000:
        quotient, remainder = divmod(number, 1000)

    # If the remainder is in the dictionary, append it to the results
    if remainder in roman_numerals:
        return roman_numerals[quotient] + roman_numerals[remainder]

    # If the remainder isn't in the dictionary, then we know it's a combination of roman numerals.
    # If the quotient isn't a multiple of 10, then the remainder is one of the values and
    # we don't have to consider any further quotients.
    else:
        if quotient % 10 != 0:
            return roman_numerals[quotient]

        # If the remainder is a multiple of 10, then we need to consider any quotients that may exist.
        # If the quotient is in the dictionary, append it to the results
        elif quotient in roman_numerals:
            return roman_numerals[quotient]

        # If the quotient isn't in the dictionary, then we know it's a combination of roman numerals.
        # If the quotient modulus 100 is 0, then the remainder is one of the values and
        # we don't have to consider any further quotients.
        elif quotient % 100 == 0:
            if remainder in roman_numerals:
                return roman_numerals[remainder]
            else:
                return roman_numerals[quotient // 10] +
