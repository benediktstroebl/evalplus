
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
    if not 0 < number <= 1000:
        raise ValueError('number must be between 1 and 1000')

    # Create a dictionary that maps each of the 12 pairs of digits
    # to its corresponding roman numeral.
    # (this dictionary does not include the 5's, since we will treat them as special cases)
    numbers = {(1, 4, 9): 'i', (1, 5, 9): 'v', (1, 6, 9): 'x',
               (1, 8, 9): 'l', (1, 7, 9): 'l', (1, 3, 9): 'm',
               (1, 2, 9): 'm', (1, 2, 8): 'd', (1, 2, 7): 'd',
               (1, 2, 6): 'c', (1, 2, 5): 'c', (1, 2, 4): 'c',
               (1, 2, 3): 'c', (1, 2, 2): 'c', (1, 2, 1): 'c',
               (1, 2, 0): 'c', (1, 1, 9): 'm', (1, 1, 8): 'd',
               (1, 1, 7): 'd', (1, 1, 6): 'c', (1, 1, 5): 'l',
               (1, 1, 4): 'l', (1, 1, 3): 'x', (1, 1, 2): 'x',
               (1, 1, 1): 'x', (1, 1, 0): 'x'}

    # Create a string to hold the answer
    # (this is where we will put the roman numeral string)
    roman_string = ''

    # While the number is nonzero...
    while number != 0:
        # Find the largest pair of digits that is less than or equal to the last digit of the number.
        # (If the number is less than 12, then there is no
