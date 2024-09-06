
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
    assert isinstance(number, int)
    assert number >= 1 and number <= 1000

    # Shortcuts for the simple cases
    if number <= 3:
        return number * 'i'
    if number == 4:
        return 'iv'
    if number == 9:
        return 'ix'

    # Set up the remainder of the number to be handled
    remainder = number
    result = ''

    # This list contains the pairs of numbers and their roman representation
    pairs = [(1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'), (100, 'c'),
             (90, 'xc'), (50, 'l'), (40, 'xl'), (10, 'x'), (9, 'ix'),
             (5, 'v'), (4, 'iv'), (1, 'i')]

    # Handle the pairs, one at a time
    for pair in pairs:
        while remainder >= pair[0]:
            remainder -= pair[0]
            result += pair[1]

    return result
