
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
    # create a dictionary with keys from 1 to 1000
    dict = {
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
        30: 'xl',
        40: 'xc',
        50: 'xc',
        60: 'xc',
        70: 'xc',
        80: 'xc',
        90: 'xc',
        100: 'xc',
        500: 'cd',
        1000: 'm'
    }
    num = str(number)
    if len(num) == 1:
        return dict[1]
    if len(num) == 2:
        if number == 10:
            return dict[10]
        else:
            return dict[int(num[1])] + dict[int(num[0])]
    if number < 1000:
        return dict[10 ** (len(num) - 1)] + int_to_mini_roman(int(num[1:]))
    return ""

