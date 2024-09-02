
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
    # your code here
    d = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}
    result = ''
    temp = number
    for i in range(1, 7):
        if temp // (10 ** i) >= 1:
            k = (temp // (10 ** i)) * (10 ** (i - 1))
            result += d[k]
            temp -= k
    return result.lower()

