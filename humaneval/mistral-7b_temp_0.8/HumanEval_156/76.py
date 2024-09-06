
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


    if number == 1:
        return 'i'
    if number == 2:
        return 'ii'
    if number == 3:
        return 'iii'
    if number == 4:
        return 'iv'
    if number == 5:
        return 'v'
    if number == 6:
        return 'vi'
    if number == 7:
        return 'vii'
    if number == 8:
        return 'viii'
    if number == 9:
        return 'ix'
    if number == 10:
        return 'x'
    if number == 20:
        return 'xx'
    if number == 30:
        return 'xxx'
    if number == 40:
        return 'xl'
    if number == 50:
        return 'l'
    if number == 60:
        return 'lx'
    if number == 70:
        return 'lxx'
    if number == 80:
        return 'lxx'
    if number
