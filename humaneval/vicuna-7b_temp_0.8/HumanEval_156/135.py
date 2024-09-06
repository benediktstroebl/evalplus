
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
    roman = ''
    while number >= 1000:
        roman = RomanNumeral.roman_to_number(roman, number)
        number -= 1000
    roman = RomanNumeral.roman_to_number(roman, number)
    return roman.lower()

@register_callable('md5')
