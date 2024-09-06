
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
    roman_numeral = ''
    if number >= 1000:
        roman_numeral += '_'
    if number >= 900:
        roman_numeral += 'CD'
    if number >= 800:
        roman_numeral += 'D'
    if number >= 700:
        roman_numeral += 'CM'
    if number >= 600:
        roman_numeral += 'XC'
    if number >= 500:
        roman_numeral += 'L'
    if number >= 400:
        roman_numeral += 'XLIX'
    if number >= 300:
        roman_numeral += 'XXX'
    if number >= 200:
        roman_numeral += 'XCIX'
    if number >= 100:
        roman_numeral += 'C'
    if number >= 90:
        roman_numeral += 'XC'
    if number >= 80:
        roman_numeral += 'L'
    if number >= 70:
        roman_numeral += 'XL'
    if number >= 60:
        roman_numeral += 'X'
    if number >= 50:
        roman_numeral += 'V'
    if number >= 40:
        roman_numeral += 'IV'
    if number >= 30:
        roman_numeral += 'III'
    if number >= 20:
        roman_numeral += 'II'
    if number >= 10:
        roman_numeral += 'I'
    return roman_numeral.lower()
