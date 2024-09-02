
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

    # Dict of integers and their roman numeral equivalents
    int_to_roman = {
        1 : 'i',
        5 : 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm',
    }

    roman = ''
    num = number
    # Loop through the 3 digit numbers
    for power in range(2, -1, -1):
        base = 10**power
        # Get the roman numeral equivalent of the current digit
        digit = int_to_roman[base]
        # Find the number of times that digit occurs
        while num >= base:
            num -= base
            roman += digit
    return roman

