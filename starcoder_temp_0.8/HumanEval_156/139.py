
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
    assert 1 <= number <= 1000
    return ''.join(ROMAN_NUMERALS[number % 10 ** (len(ROMAN_NUMERALS) - i) // (10 ** (len(ROMAN_NUMERALS) - i - 1))] for i in range(1, len(ROMAN_NUMERALS) + 1))
