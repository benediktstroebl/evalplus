
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

    # Initialize empty string
    roman = ''

    # Initialize a dictionary containing the roman symbols and their values
    symbols = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

    # Loop over the dictionary keys
    for key in symbols:
        # Find the largest multiple of key that divides the number
        multiple = number // symbols[key]

        # Add that number of key's to the string
        roman += key * multiple

        # Subtract the multiple from the number
        number -= symbols[key] * multiple

    return roman


