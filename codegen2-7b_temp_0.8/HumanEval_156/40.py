
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
    result = ""
    for i in range(1, number + 1):
        if i < 4:
            result += "i"
        elif i < 9:
            result += "v"
        elif i == 9:
            result += "ix"
        elif i == 10:
            result += "x"
        elif i == 11:
            result += "xi"
        elif i == 12:
            result += "l"
        elif i == 13:
            result += "xc"
    return
