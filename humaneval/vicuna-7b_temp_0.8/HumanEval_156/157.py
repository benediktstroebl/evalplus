
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
    numerals = ['I', 'V', 'X', 'L', 'XL', 'XC', 'CD', 'CX', 'CM', 'D', 'DX', 'IX', 'XLV', 'LV', 'XL', 'X', 'IV', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XL', 'XLI', 'XLII', 'XLIII', 'XLIV', 'XLV', 'L', 'LX', 'LXX', 'LXXX', 'LXIX']
    roman_numeral = ''
    value = number
    while value != 0:
        numeral = numerals.pop(0)
        value = value // 10
        roman_numeral += numeral
    return roman_numeral.lower()

