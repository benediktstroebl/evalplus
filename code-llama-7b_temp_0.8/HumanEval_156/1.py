
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
    if number <= 0:
        raise ValueError('Please enter a positive number')

    # use a dictionary to map the numbers to the corresponding roman numerals
    roman_numerals = {
        1000: 'm',
        500: 'd',
        100: 'c',
        50: 'l',
        10: 'x',
        5: 'v',
        1: 'i',
    }

    roman_num_str = ''
    for key in sorted(roman_numerals, reverse=True):
        if number < key:
            continue
        else:
            num_to_append = number // key
            roman_num_str += roman_numerals[key] * num_to_append
            number %= key
            continue

    return roman_num_str

