
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
    roman_numeral = []
    numerator = number // 1000
    remainder = number % 1000
    numerator_str = str(numerator).zfill(2)
    numerator_abs = int(numerator_str[:-2])
    while numerator != 0:
        numerator_str = str(numerator).zfill(2)
        numerator_abs = int(numerator_str[:-2])
        numerator = remainder // 100
        remainder = remainder % 100
        roman_numeral.append(numerator_str[0])
        roman_numeral.append(numerator_str[1])
    roman_numeral.append(numerator_abs)
    return ' '.join(roman_numeral)
