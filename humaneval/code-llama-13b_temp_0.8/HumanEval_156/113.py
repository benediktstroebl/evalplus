
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
    num_to_roman_map = {
        1: 'i',
        5: 'v',
        10: 'x',
        50: 'l',
        100: 'c',
        500: 'd',
        1000: 'm'
    }

    roman_numeral = ''
    # Traverse from the highest to the lowest
    for value, letter in sorted(num_to_roman_map.items(), reverse=True):
        if number >= value:
            # Find the count of times that value goes into number
            count = number // value
            number -= count * value
            roman_numeral += letter * count

    return roman_numeral

