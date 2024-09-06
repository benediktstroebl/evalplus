
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
    if number > 1000 or number <= 0:
        return 'Invalid input'
    d = [1000, 500, 100, 50, 10, 5, 1]
    r = ['m', 'd', 'c', 'l', 'x', 'v', 'i']
    result = []
    for i in range(7):
        if number < d[i]:
            continue
        q = number // d[i]
        result.append(r[i] * q)
        number %= d[i]
    return ''.join(result)

