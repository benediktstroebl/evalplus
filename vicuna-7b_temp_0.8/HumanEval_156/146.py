
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
    if number < 1000:
        return f"{number}i"

    # convert 1000, 900, 800, ..., 400 to ii, iii, iv, ..., xvi
    if number >= 1000 and number <= 1000:
        return 'ii'
    if number >= 900 and number <= 900:
        return 'iii'
    if number >= 800 and number <= 800:
        return 'iv'
    if number >= 700 and number <= 700:
        return 'v'
    if number >= 600 and number <= 600:
        return 'vi'
    if number >= 500 and number <= 500:
        return 'vii'
    if number >= 400 and number <= 400:
        return 'viii'
    if number >= 300 and number <= 300:
        return 'ix'
    if number >= 200 and number <= 200:
        return 'x'
    if number >= 100 and number <= 100:
        return 'xi'
    return 'x'
