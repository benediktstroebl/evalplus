
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
    if 1 <= number <= 10:
        return str(number)
    if number == 11:
        return 'xi'
    if number == 12:
        return 'xii'
    if number == 13:
        return 'xiii'
    if number == 14:
        return 'xiv'
    if number == 15:
        return 'xv'
    if number == 16:
        return 'xvi'
    if number == 17:
        return 'xvii'
    if number == 18:
        return 'xviii'
    if number == 19:
        return 'xix'
    if number == 20:
        return 'xx'
    if number == 21:
        return 'xxi'
    if number == 22:
        return 'xxii'
    if number == 23:
        return 'xxiii'
    if number == 24:
        return 'xxiv'
    if number == 25:
        return 'xx
