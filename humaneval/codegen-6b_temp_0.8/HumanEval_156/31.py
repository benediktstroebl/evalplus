
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
    if number < 1 or number > 1000:
        raise ValueError('Number must be in [1, 1000]')

    # Initialize dictionary of strings for roman numerals
    
    d = {'m': 1000, 'cm': 900, 'd': 500, 'cd': 400,
         'c': 100, 'xc': 90, 'l': 50, 'xl': 40,
         'v': 5, 'xv': 10, 'i': 1}

    # Initialize string to append
    # This string will be reversed at the end

    string = ''

    # Loop over each roman numeral in reverse order
    
    for roman in sorted(d, reverse=True):
        # Test if the remainder is zero
        
        if number >= d[roman]:
            # If so, append the roman numeral
            
            string = roman + string
            # Subtract the roman numeral from the number
            
            number -= d[roman]

    # Return string in all lowercase
    
    return string.lower()

