
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
    roman_chars = [
        'I', 'V', 'X', 'L', 'C', 'D', 'M', 'N', 'XL', 'LX', 'LXX', 'LXXX', 'XC',
        'CD', 'D', 'CX', 'CM', 'XCIX', 'CDXIX', 'CXXV', 'CXXVI', 'XXXV', 'XLV',
        'LV', 'IV', 'I'
    ]

    num_chars = [
        '', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII',
        'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII',
        'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XL', 'XLI', 'XLII', 'XLIII',
        'XLIV', 'XLV', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'XCV', 'CD', 'D', 'C', 'CM',
        'XCIX', 'CDXIX', 'CXXV', 'CXXVI', 'XXXV', 'XLV', 'LV', 'IV', 'I'
    ]

    roman_number = []
    while number > 0:
        divisor = 10
        while divisor > 0:
            if number % divisor == 0:
                roman_number.insert(0, roman_chars[divisor - 1])
                number /= divisor
                break
            divisor /= 10
        else:
            roman_number.insert(0, roman_chars[number - 1])
            break

    return ''.join(roman_number)