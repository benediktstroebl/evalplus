
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
    # This list holds the symbols that make up the 'roman numeral'
    # for each integer value. The value of each symbol tells us how many
    # of that symbol there should be for the integer value of the symbol minus one.
    # The first value is in the list.
    symbol_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    # The list of all symbols corresponding to the symbols in the list above.
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    # Initialize a string to hold our resulting roman numeral.
    mini_roman = ''
    # Loop over the list, starting at index zero, and incrementing index by
    # the number of symbols in the symbol_values list at the same index.
    for i in range(len(symbol_values)):
        # This is a temp variable for the integer value of the current symbol.
        temp = number // symbol_values[i]
        # If the current symbol is X, temp will take the value of 1.
        # Otherwise, temp will take the value of the value of the current symbol minus one.
        if temp == 1:
            # Add the symbol to our roman numeral, and reset temp.
            mini_roman += symbols[i]
            temp = 0
        # Add all of the symbols that make up the current symbol to our roman numeral,
        # and reset temp to zero.
        while temp > 0:
            # If we are at the end of the list, then we can just add to the roman numeral string.
            if i == len(symbol_values) - 1:
                mini_roman += symbols[i]
                temp -= 1
            # We do not want to add the symbol to the roman numeral string.
            # Instead, we want to assign the value of the symbol minus one to the temp variable.
            elif temp > 0:
                mini_roman += symbols[i]
                temp -= 1
    # Return our roman numeral string, in lowercase.
