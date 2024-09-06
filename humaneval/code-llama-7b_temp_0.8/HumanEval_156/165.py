
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

    int_to_roman = lambda n: 'x' * n if n == 1 else 'c' * n if n == 100 else 'c' * (n // 100) + 'l' * ((n // 10) % 10) + 'x' * (n % 10)

    return int_to_roman(number).lower()
