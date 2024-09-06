
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
    roman_mapping = [
        ['', 'I', 'V', 'X', 'L', 'XL', 'XC', 'CD', 'D'],
        ['', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
        ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DX', 'DXX', 'DXXX', 'CD']
    ]
    numeral = str(number)
    numeral = numeral.upper()
    numeral_length = len(numeral)
    result = ''
    for i in range(numeral_length):
        digit = numeral[i:i+1]
        result = roman_mapping[digit.index('I')] + result
    return result.lower()
