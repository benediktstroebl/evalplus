
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
    roman_map = {'I': 'X', 'V': 'IV', 'X': 'IX', 'L': 'V',
                 'XL': 'XCVI', 'XC': 'XC', 'CD': 'C', 'CX': 'CI',
                 'D': 'XLIV', 'DX': 'XLV', 'II': 'II', 'IV': 'IV',
                 'IX': 'IX', 'VIII': 'VIII', 'VII': 'VII',
                 'VI': 'VI', 'V': 'V', 'IV': 'IV', 'III': 'III',
                 'II': 'II', 'I': 'I'}
    roman_num = ''
    while number > 0:
        digit = number % 10
        number /= 10
        if digit >= '0' and digit <= '9':
            roman_num += str(digit)
        else:
            roman_num += roman_map[str(digit)]
        if number == 0:
            break
    return roman_num.lower()
