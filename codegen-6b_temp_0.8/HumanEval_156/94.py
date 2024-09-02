
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
    # Initialise dictionary of roman numerals from index to value
    romans = {
        1: 'x',
        2: 'c',
        3: 'm',
        4: 'd',
        5: 'v',
        6: 'net',
        7: 'c',
        8: 'l',
        9: 'x',
        10: 'm',
        11: 'c',
        12: 'x',
        13: 'm',
        14: 'c',
        15: 'x',
        16: 'x',
        17: 'x',
        18: 'x',
        19: 'x',
    }
    # Loop over each unit, starting from the largest and working our way down
    output, i = '', 19
    while i >= 1:
        # Add the roman numeral equivalent of the integer, starting with the
        # largest unit
        output += romans[i]
        # Subtract the value of the integer from the current unit, for the next
        # iteration
        i -= i
    return output.lower()

