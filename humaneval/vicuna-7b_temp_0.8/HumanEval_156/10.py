
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
    for i in range(1, 1000):
        roman = f'{roman}{i:d}' if i in [100, 900, 1000] else f'{roman}{i}'
    roman = f'{roman}{number}' if number in [100, 900, 1000] else f'{roman}{number}'
    return roman.lower()