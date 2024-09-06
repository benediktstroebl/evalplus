
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
        raise ValueError('Only positive integers between 1 and 1000 are allowed')

    romans = {
        1: 'i',
        2: 'x',
        3: 'c',
        4: 'm',
        5: 'v',
        6: 'l',
        7: 'd',
        8: 'o',
        9: 's',
        10: 'p',
        20: 'v',
        30: 'l',
        40: 'c',
        50: 'd',
        60: 'h',
        70: 'r',
        80: 't',
        90: 's',
    }

    # Dicts don't have a sorted method so we'll resort to a list
    sorted_roman_keys = sorted(romans.keys(), reverse=True)

    result = []
    for key in sorted_roman_keys:
        while number >= key:
            result.append(romans[key])
            number -= key

    # Remove duplicates
    return ''.join(dict.fromkeys(result))
