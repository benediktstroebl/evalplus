
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
    roman_numerals = [
        '', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX',
        'X', 'XI', 'XII', 'XIII', 'IV', 'IX', 'X', 'XL', 'XLI', 'XLII',
        'XLIII', 'XLIV', 'XLV', 'XLVI', 'XLVII', 'XLVIII', 'XLIX', 'L',
        'LI', 'LII', 'LIII', 'LIV', 'LV', 'LVI', 'LVII', 'LVIII', 'LIX',
        'LX', 'LXI', 'LXII', 'LXIII', 'LXIV', 'LXV', 'LXVI', 'LXVII',
        'LXVIII', 'LXIX', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC',
        'DCCC', 'CM', 'CM'
    ]
    roman_numeral = [roman_numerals[i] for i in str(number)]
    return roman_numeral[0] + '.' + roman_numeral[1]
