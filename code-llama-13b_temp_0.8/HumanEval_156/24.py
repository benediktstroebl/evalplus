
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
    # map of integers to their roman representations
    num_to_roman = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm'
    }

    # keys are in descending order
    keys = sorted(num_to_roman.keys(), reverse=True)
    roman = ''
    for key in keys:
        # get the roman representation of this key,
        # then keep removing it from the number until
        # we cannot represent this key any more.
        # For example, when key = 100, while num is still larger than 100,
        # roman += num_to_roman[key] will be 'c', and num -= 100 will be 426 - 100 = 326
        # In the next iteration, key = 100 again, but num is not 426 any more, so the loop
        # terminates, and roman becomes 'cdxxvi'
        while number >= key:
            roman += num_to_roman[key]
            number -= key
    return roman.lower()

