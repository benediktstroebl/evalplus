
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
    symbols = [
        '', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX',
        'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII',
        'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI',
        'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XL', 'L', 'LII', 'LIII',
        'LIV', 'LV', 'LVI', 'LVII', 'LVIII', 'LIX', 'LX', 'LXI', 'LXII',
        'LXIII', 'LXIV', 'LXV', 'LXVI', 'LXVII', 'LXVIII', 'LXIX', 'C',
        'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'CX', 'CM', 'M', 'MM',
        'DCCC', 'CMX', 'XC', 'XL', 'XLI', 'XLIV', 'L', 'LX', 'LXXX',
        'LXXXX', 'LXIX', 'XCVI', 'CV', 'CVI', 'MC', 'MMC', 'MCC', 'MX',
        'XC', 'XLV', 'XLVI', 'XLVII', 'XLVIII', 'XLIX', 'LI', 'LII',
        'LIII', 'LIV', 'LV', 'LVI', 'LVII', 'LVIII', 'LIX', 'LX', 'LXI',
        'LXII', 'LXIII', 'LXIV', 'LXV', 'LXVI', 'LXVII', 'LXVIII', 'LXIX',
        'CMXI', 'CMX', 'XCIX', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC',
        'CX', 'CM', 'M', 'MM', 'DCCC
