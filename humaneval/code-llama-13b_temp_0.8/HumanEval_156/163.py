
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
    M = ['m', 'd', 'c', 'l', 'x', 'v', 'i']
    N = [1000, 500, 100, 50, 10, 5, 1]
    roman = ''
    for i in range(len(N)):
        if number // N[i] > 0:
            number -= N[i]
            roman += M[i] * (number // N[i])
            number = number % N[i]
    return roman.lower()

