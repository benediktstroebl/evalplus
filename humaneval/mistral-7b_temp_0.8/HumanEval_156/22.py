
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
    roman_num = 'I'
    ones_map = {1: roman_num, 5: 'V', 10: 'X', 50: 'L', 100: 'C'}
    five_map = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C'}
    tens_map = {1: 'I', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    ones_sum = 0
    five_sum = 0
    tens_sum = 0

    # Sum up the values in the map.
    for x in ones_map:
        if number >= x:
            ones_sum += x
            number -= x
    for x in five_map:
        if number >= x:
            five_sum += x
            number -= x
    for x in tens_map:
        if number >= x:
            tens_sum += x
