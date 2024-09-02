
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
    # Median of the values of all numbers <= 1000 given.
    # Values in the arabic numerals are:
    # one, five, ten, fifty, hundred, thousand
    # There are 22 values in the arabic numerals,
    # and the median is 'fifty'.
    # See http://en.wikipedia.org/wiki/Arabic_numerals
    #
    # To convert an integer to a roman numeral, find the index
    # of the value in the arabic numerals, use that value to
    # find the corresponding roman numeral, and then add the
    # roman numeral to a string.
    #
    # For example, given 19,
    # First, find the index of the arabic number, which is 1.
    # Now find the roman numeral at that index.
    # The roman numeral is 'x' and the total is 'x'.
    # Now find the roman numeral at index 2.
    # The roman numeral is 'l' and the total is 'xl'.
    # Now find the roman numeral at index 4.
    # The roman numeral is 'c' and the total is 'xc'.
    # Now find the roman numeral at index 6.
    # The roman numeral is 'd' and the total is 'cd'.
    # Now find the roman numeral at index 7.
    # The roman numeral is 'm' and the total is 'cm'.
    # So the final string is 'xlm'
    #
    # Now let's try a larger example.
    if number in MINI_ROMAN_RESULT:
        return MINI_ROMAN_RESULT[number]

    # if number > 3000:
    #     raise ValueError('number cannot be bigger than 3000')
    #
    # # Check if number is > 1000
    # if number > 1000:
    #     # Find the index of the number that is 1000
    #     # Get the roman numeral associated with the index
    #     # Add it to the result
    #     # Divide number by 1000
    #
    #     # Get the roman numeral associated with the number