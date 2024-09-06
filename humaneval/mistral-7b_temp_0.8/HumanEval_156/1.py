
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
    m1, m2, m3, m4, m5 = '', '', '', '', ''
    m1, m2, m3, m4, m5 = 'm', 'c', 'x', 'l', 'v'
    d1, d2, d3, d4, d5 = 'd', 'l', 'x', 'v', 'i'
    if 1000 <= number:
        return 'm' + d5 * (number // 1000)
    if number > 900:
        return m1 + d5 * ((number - 900) // 100)
    if number > 400:
        return m2 + d4 * ((number - 400) // 100)
    if number > 90:
        return m2 + d5 * ((number - 90) // 10)
    if number > 40:
        return m3 + d3 * ((number - 40) // 10)
    if number > 9:
        return m3 + d
