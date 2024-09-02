
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
    if number == 1000:
        return "m"
    if number == 900:
        return "cm"
    if number == 500:
        return "d"
    if number == 400:
        return "cd"
    if number == 100:
        return "c"
    if number == 90:
        return "xc"
    if number == 50:
        return "l"
    if number == 40:
        return "xl"
    if number == 10:
        return "x"
    if number == 9:
        return "ix"
    if number == 5:
        return "v"
    if number == 4:
        return "iv"
    if number == 1:
        return "i"
    return ""

