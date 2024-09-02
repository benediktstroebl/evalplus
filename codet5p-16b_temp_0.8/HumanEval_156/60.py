
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

    if not isinstance(number, int) or number > 1000 or number < 1:
        return None
    roman = ''
    thousands, hundreds, tens, ones = 0, 0, 0, 0

    while number > 0:
        thousands = number // 1000
        number %= 1000
        hundreds = number // 100
        number %= 100
        tens = number // 10
        number %= 10
        ones = number
        roman = roman + ''.join(int_to_mini_roman_numeral(thousands))
        roman = roman + ''.join(int_to_mini_roman_numeral(hundreds))
        roman = roman + ''.join(int_to_mini_roman_numeral(tens))
        roman = roman + ''.join(int_to_mini_roman_numeral(ones))
    return roman.lower()

