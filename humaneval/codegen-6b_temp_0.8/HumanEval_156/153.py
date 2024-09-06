
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
    translation = {
        1: 'i',
        2: 'ii',
        3: 'iii',
        4: 'iv',
        5: 'v',
        6: 'vi',
        7: 'vii',
        8: 'viii',
        9: 'ix',
        10: 'x',
        11: 'xi',
        12: 'xii',
        13: 'xiii',
        14: 'xiv',
        15: 'xv',
        16: 'xvi',
        17: 'xvii',
        18: 'xviii',
        19: 'xix',
        20: 'x',
        30: 'l',
        40: 'c',
        50: 'd',
        60: 'm',
        70: 'r',
        80: 'lx',
        90: 'b',
        100: 'm',
        101: 'cm',
        102: 'd',
        103: 'cd',
        104: 'c',
        105: 'c',
        106: 'o',
        107: 'co',
        108: 'o',
        109: 'x',
        110: 'x',
        111: 'x',
        112: 'xe',
        113: 'x',
        114: 'x',
        115: 'x',
        116: 'x',
        120: 'z',
        400: 'm',
        500: 'c',
        600: 'd',
        700: 'm',
        800: 'x',
        900: 'l',
        1000: '',
    }

    if number > 1000:
        raise ValueError('number cannot be greater than 1000')

    if number <= 0:
        raise ValueError('number cannot be negative')

    res = []
    for i in range(1, number + 1):
        res.append(translation[i])

    return ''.join(res)

