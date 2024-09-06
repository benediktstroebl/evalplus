
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
    if number > 1000 or number < 1:
        raise ValueError('num must be between 1 and 1000')

    roman = ''
    romans = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}
    for symbol in sorted(romans.keys(), reverse=True):
        while number >= symbol:
            roman += romans[symbol]
            number -= symbol

    return roman.lower()

