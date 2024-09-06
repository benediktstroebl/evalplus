
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
    elif number == 10:
        return 'x'
    elif number == 11:
        return 'xi'
    elif number == 12:
        return 'xii'
    elif number == 13:
        return 'xiii'
    elif number == 14:
        return 'xiv'
    elif number == 15:
        return 'xv'
    elif number == 16:
        return 'xvi'
    elif number == 17:
        return 'xvii'
    elif number == 18:
        return 'xviii'
    elif number == 19:
        return 'xix'
    elif number == 20:
        return 'xx'
    elif number == 21:
        return 'xxi'
    elif number == 22:
        return 'xxii'
    elif number == 23:
        return 'xxiii'
    elif number == 24:
        return 'xxiv'
    elif number == 25:
        return 'xxv'
    elif number == 26:
        return 'xxvi'
    elif number == 27:
        return 'xxvii'
    elif number == 28:
        return 'xxviii'
    elif number == 29:
        return 'xxix'
    elif number == 30:
        return 'xxx'
    elif number == 31:
        return 'xxi'
    elif number == 32:
        return 'xxii'
    elif number == 33:
        return 'xxiii'
    elif number == 34:
        return 'xxiv'
    elif number == 35:
        return 'xxv'
    elif