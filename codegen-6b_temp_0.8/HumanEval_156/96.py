
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
    # create dictionary of integer-value: roman-value pairs
    d = {1: 'i', 2: 'ii', 3: 'iii', 4: 'iv', 5: 'v', 6: 'vi', 7: 'vii', 8: 'viii', 9: 'ix', 10: 'x',
         11: 'xi', 12: 'xii', 13: 'xiii', 14: 'xiv', 15: 'xv', 16: 'xvi', 17: 'xvii', 18: 'xviii', 19: 'xix'}

    # build the roman numeral string
    roman_numeral = ''
    for i in range(1, max(d.keys())):
        if number >= i:
            roman_numeral += d[i]
            number -= i

    return roman_numeral

