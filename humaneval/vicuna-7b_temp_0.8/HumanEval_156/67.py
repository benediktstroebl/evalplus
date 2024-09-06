
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
    roman_chars = 'IVXLCDM'

    roman = ''

    for num in range(10):
        roman += roman_chars[num]

    if number >= 100:
        roman += str(number)[-2:]
    else:
        roman += str(number)[-1:]

    return roman.lower()
