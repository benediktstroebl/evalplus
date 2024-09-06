
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
    roman_map = {'I': 'X', 'V': 'V', 'X': 'X', 'L': 'X', 'C': 'CV', 'D': 'CD',
                 'M': 'CM', 'N': 'XC', 'R': 'RX', 'S': 'SX', 'T': 'TX',
                 'H': 'XX', 'G': 'XL', 'F': 'L', 'P': 'XXX', 'B': 'XXX',
                 'Q': 'XXXX', 'Z': 'XXX', 'Y': 'YYY', 'W': 'VII',
                 'V': 'IV', 'X': 'I', 'L': 'V', 'C': 'I', 'D': 'V',
                 'M': 'X', 'N': 'V', 'R': 'I', 'S': 'V', 'T': 'I',
                 'H': 'V', 'G': 'IV', 'F': 'I', 'P': 'VII', 'B': 'XLI',
                 'Q': 'XLV', 'Z': 'XL', 'Y': 'XXX', 'W': 'VII', 'V': 'VII',
                 'X': 'VII', 'L': 'VII', 'C': 'VII', 'D': 'VII', 'M': 'VII',
                 'N': 'VII', 'R': 'VII', 'S': 'VII', 'T': 'VII', 'H': 'VII',
                 'G': 'VII', 'F': 'VII', 'P': 'VII', 'B': 'VI', 'Q': 'V',
                 'Z': 'IV', 'Y': 'II', 'W': 'I', 'V': 'I', 'X': 'I', 'L': 'V',
                 'C': 'I', 'D': 'V', 'M': 'I', 'N': 'I', 'R': 'I', 'S': 'V',
                 'T': 'I', 'H': 'I', 'G': 'I', 'F': 'I', 'P': 'II', 'B': 'X',
                 'Q': 'V', 'Z': 'I', 'Y':
