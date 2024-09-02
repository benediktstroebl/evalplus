
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
    roman_chars = 'VIIVIIIVIIVIIVIII'
    result = []
    while number > 0:
        number, remainder = divmod(number, 100)
        result.insert(0, roman_chars[remainder])
    return ''.join(reversed(result))
