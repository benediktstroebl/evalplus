
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
    numerals = 'I V X L C D M D'
    roman_num = ''
    for i in range(len(numerals) - len(str(number)) + 1):
        roman_num += numerals[number % 10]
        number //= 10
    return roman_num[::-1].lower()
