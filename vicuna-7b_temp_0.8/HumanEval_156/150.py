
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
    roman_numerals = {
        'I': 'i', 'II': 'ii', 'III': 'iii',
        'IV': 'iv', 'V': 'v', 'VI': 'vi',
        'VII': 'vii', 'VIII': 'viii', 'IX': 'ix',
        'X': 'x', 'XI': 'xi', 'XII': 'xii',
        'XIII': 'xiii', 'XIV': 'xiv', 'XV': 'xv',
        'XVI': 'xvi', 'XVII': 'xvii', 'XVIII': 'xviii',
        'XIX': 'xix', 'XX': 'xx', 'XXI': 'xxi',
        'XXII': 'xxii', 'XXIII': 'xxiii', 'XXIV': 'xxiv',
        'XXV': 'xxv', 'XXVI': 'xxvi', 'XXVII': 'xxvii',
        'XXVIII': 'xxviii', 'XXIX': 'xxix', 'XXX': 'xxx'
    }

    number = int(number)
    numerator = number
    denominator = 1000

    while denominator != 0:
        numerator /= denominator
        denominator /= 1000

    roman_numeral = ''

    while numerator != 0:
        digit = numerator % 10
        numerator = numerator // 10
        roman_numeral = roman_numerals[digit] + roman_numeral

    return roman_numeral.lower()