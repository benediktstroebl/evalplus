
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
    less_than_20 = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']
    less_than_100 = ['', 'x', 'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii', 'xix']
    less_than_1000 = ['', 'x', 'l', 'lx', 'lxx', 'lxxx', 'lxxxx', 'xl', 'xlx', 'xlxx', 'xlxxx', 'xllxxx', 'xllxxxx', 'xllxxxi', 'xllxxii', 'xllxxiii', 'xllxxiv', 'xllxxv', 'xllxxvi', 'xllxxvii', 'xllxxviii', 'xllxxix', 'xllxx', 'ccc']
    if number < 20:
        return less_than_20[number]
    if number < 100:
        return less_than_100[number]
    if number < 1000:
        return less_than_1000[number]

