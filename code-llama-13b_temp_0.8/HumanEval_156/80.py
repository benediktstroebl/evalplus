
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
    if type(number) != int:
        raise TypeError("input must be an integer")
    if number < 0 or number > 1000:
        raise ValueError("number out of range (must be 0 < number <= 1000)")

    # these strings will be concatenated to the result
    result = []
    # string representations of numbers from 1 to 1000
    # used to build up the result
    digits = (
        'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix',
        'x', 'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii', 'xix',
        'xx', 'xxi', 'xxii', 'xxiii', 'xxiv', 'xxv', 'xxvi', 'xxvii', 'xxviii', 'xxix',
        'xxx', 'xxxi', 'xxxii', 'xxxiii', 'xxxiv', 'xxxv', 'xxxvi', 'xxxvii', 'xxxviii', 'xxxix',
        'xl', 'xli', 'xlii', 'xliii', 'xliv', 'xlv', 'xlvi', 'xlvii', 'xlviii', 'xlix',
        'l', 'li', 'lii', 'liii', 'liv', 'lv', 'lvi', 'lvii', 'lviii', 'lix',
        'lv', 'lvi', 'lvii', 'lviii', 'lix',
        'lv', 'lvi', 'lvii', 'lviii', 'lix',
        'c', 'ci', 'cii', 'ciii', 'civ', 'cv', 'cvi', 'cvii', 'cviii', 'cix',
        'c', 'ci', 'cii', 'ciii', 'civ', 'cv', 'cvi', 'cvii', 'cviii', 'cix',
        'c', 'ci', 'cii', 'ciii', 'civ', 'cv', 'cvi', 'cvii', 'cvi
