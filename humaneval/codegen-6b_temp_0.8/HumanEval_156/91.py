
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
    if not (isinstance(number, int) and 1 <= number <= 1000):
        raise ValueError('Input should be a positive integer between 1 and 1000')

    # Initialize the output
    letters = []

    # Generate each symbol in roman numerals
    for symbol, value in SYMBOLS.iteritems():

        # If this symbol exceeds the input, no more
        # conversion can be done
        if number < value:
            break

        # If the input is equal to the value of the symbol
        # add it to the output
        if number == value:
            letters += [symbol]
            break

        # Add the necessary number of symbols to the
        # output
        letters += [symbol] * (number / value)

        # Subtract the necessary number of symbols
        # from the input
        number %= value

    return ''.join(letters).lower()

