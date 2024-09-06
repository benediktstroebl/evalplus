
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

    ROMAN_NUMERALS = [
        ('', '', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix'),
        ('', 'x', 'xi', 'xii', 'xiii', 'xiv', 'xv', 'xvi', 'xvii', 'xviii', 'xix')
    ]
    number = int(number)
    assert 1 <= number <= 1000, 'The number has to be between 1 and 1000.'
    result = ''
    for i in range(2):
        result += ROMAN_NUMERALS[i][number // 10 ** (i+1) % 10]
    return result.lower()
