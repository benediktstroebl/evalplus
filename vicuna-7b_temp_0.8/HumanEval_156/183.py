
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
    roman_mapping = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XL', 'L', 'L', 'L', 'L', 'L', 'C', 'D', 'D', 'D', 'M', 'M', 'M', 'M', 'M', 'D', 'X', 'C', 'X', 'I', 'V', 'IV', 'I', 'VII', 'VI', 'V']

    numeral = str(number)
    result = numeral[0]
    for char in numeral:
        if char.isdigit():
            result += char
        elif char == 'I':
            result += 'V'
        elif char == 'V':
            result += 'I'
        elif char == 'X':
            result += 'I'
        elif char == 'L':
            result += 'C'

    roman_numeral = roman_mapping[result]
    return roman_numeral.lower()