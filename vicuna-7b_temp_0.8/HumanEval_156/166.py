
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
    # Construct a list of symbols to use for the conversion
    symbols = 'I V X L C D'

    # Map the number to a roman numeral
    roman = {
        'I': 'I',
        'V': 'V',
        'X': 'X',
        'L': 'X',
        'C': 'I',
        'D': 'D'
    }.get(str(number))

    # If we didn't find a match, return the empty string
    if roman is None:
        return ''

    # Otherwise, return the roman numeral as a string
    return symbols[roman]
