
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
        return "i"
    if number == 5:
        return "v"
    if number == 10:
        return "x"
    if number == 50:
        return "l"
    if number == 100:
        return "c"
    if number == 500:
        return "d"
    if number == 1000:
        return "m"


    if number >= 4:
        return "iv" + int_to_mini_roman(number - 5)
    if number >= 9:
        return "ix" + int_to_mini_roman(number - 10)
    if number >= 40:
        return "xl" + int_to_mini_roman(number - 50)
    if number >= 90:
        return "xc" + int_to_mini_roman(number - 100)
    if number >= 400:
        return "cd" + int_to_
