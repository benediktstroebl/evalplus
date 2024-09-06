
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
    while number > 0:
        numerator = number / 1000
        number = number % 1000
        suffix = 'C' if numerator == 1000 else 'L' if numerator == 500 else \
                  'X' if numerator == 100 else 'V' if numerator == 50 else \
                  'I' if numerator == 10 else 'IX'
        roman += suffix[ord('A') - ord('a') + (suffix.find_index(str(numerator)) + 1)]
    return roman.lower()
