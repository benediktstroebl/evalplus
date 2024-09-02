
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

    romans = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000:'m', 4: 'iv', 9: 'ix', 40: 'xl', 90: 'xc', 400: 'cd', 900: 'cm', 4000:'mm'}
    if number == 1000:
        return romans[1000]
    if number == 999:
        return romans[1000] + romans[1]
    if number == 990:
        return romans[1000] + romans[100] + romans[10]
    if number == 979:
        return romans[1000] + romans[100] + romans[10] + romans[1]
    if number == 978:
        return romans[1000] + romans[100] + romans[10] + romans[9]
    if number == 967:
        return romans[1000] + romans[100] + romans[10] + romans[90]
    if number == 966:
        return romans[
