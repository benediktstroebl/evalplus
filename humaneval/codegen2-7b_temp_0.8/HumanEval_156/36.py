
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
    res = ""
    for i in range(1, number + 1):
        if i <= 9:
            res += str(i)
        elif i == 10:
            res += "x"
        elif i == 11:
            res += "ci"
        elif i == 12:
            res += "xl"
        elif i == 13:
            res += "xc"
    return res

