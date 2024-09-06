
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
    i = 1
    roms = ""
    while i <= number:
        if i <= 3:
            roms += chr(i + 96)
            i += 1
        elif i == 4:
            roms += 'iv'
            i += 1
        elif i == 9:
            roms += 'ix'
            i += 1
        else:
            i += 2

    return roms.lower()

