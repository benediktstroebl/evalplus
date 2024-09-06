
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
    index_map = {1: '', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v', 6: 'vi', 7: 'vii', 8: 'viii', 9: 'ix', 10: 'x', 11: 'xi', 12: 'xii', 13: 'xiii', 14: 'xiv', 15: 'xv', 16: 'xvi', 17: 'xvii', 18: 'xviii', 19: 'ix', 20: '', 21: 'xl', 22: 'xli', 23: 'xlii', 24: 'xliv', 25: 'xlv', 26: 'xlvi', 27: 'xlvii', 28: 'xlviii', 29: 'xliv', 30: 'xlv', 31: 'xlvi', 32: 'xlvii', 33: 'xlviii', 34: 'xliv', 35: 'xlv', 36: 'xlvi', 37: 'xlvii', 38: 'xlviii', 39: 'xliv', 40: 'xlv', 41: 'xlvi', 42: 'xlvii', 43: 'xlviii', 44: 'xliv', 45: 'xlv', 46: 'xlvi', 47: 'xlvii', 48: 'xlviii', 49: 'xliv', 50: 'xlv', 51: 'xlvi', 52: 'xlvii', 53: 'xlviii', 54: 'xliv', 55: 'xlv', 56: 'xlvi', 57: 'xlvii', 58: 'xlviii', 59: 'xliv', 60: 'xlv', 61: 'xlvi', 62: 'xlvii', 63: 'xlviii', 64: 'xliv', 65: 'xlv', 66: 'xlvi', 67: 'xlvii', 68: 'xlviii', 69: 'xliv', 70: 'xlv', 71: 'xlvi', 72: 'xlvii', 73: 'xlviii', 74: 'xliv', 75: 'xlv', 76: 'xlvi', 77: 'xlvii', 78: 'xlviii', 79: 'xliv', 80: 'xlv', 81: '