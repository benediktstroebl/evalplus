
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
    roman_dict = {"I": "i", "V": "v", "X": "x", "L": "l", "C": "c", "D": "d", "M": "m", "N": "n", "R": "r"}
    roman_string = ""
    numerator = 1
    denominator = 10
    while numerator != 0:
        numerator = numerator // denominator
        denominator = denominator // 10
        roman_string = roman_dict[str(numerator)] + roman_string
    return roman_string.lower()
