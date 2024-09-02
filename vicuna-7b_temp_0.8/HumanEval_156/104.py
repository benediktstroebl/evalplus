
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
    numerator, denominator = number // 1000, (number % 1000)
    numerator, denominator = numerator // 100, (numerator % 100)
    numerator, denominator = numerator // 10, (numerator % 10)
    numerator, denominator = numerator // 1, (numerator % 1)
    numerator, denominator = numerator, (denominator)

    roman_numeral = ''
    while numerator != 0:
        if denominator == 1:
            roman_numeral += 'M'
        elif denominator == 2:
            roman_numeral += 'CM'
        elif denominator == 5:
            roman_numeral += 'D'
        elif denominator == 10:
            roman_numeral += 'X'
        else:
            numerator, denominator = numerator // 10, (numerator % 10)
            roman_numeral += ''.join([chr(ord('M') - (denominator - 1)) for _ in range(denominator)])
    return roman_numeral.lower()
