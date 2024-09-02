
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

    mini_roman = ""
    for i in range(1, number + 1):
        if i == 1000:
            mini_roman += "m"
        elif i == 900:
            mini_roman += "cm"
        elif i == 500:
            mini_roman += "d"
        elif i == 400:
            mini_roman += "cd"
        elif i == 100:
            mini_roman += "c"
        elif i == 90:
            mini_roman += "xc"
        elif i == 50:
            mini_roman += "l"
        elif i == 40:
            mini_roman += "xl"
        elif i == 10:
            mini_roman += "x"
        elif i == 9:
            mini_roman += "ix"
        elif i == 5:
            mini_roman += "v"
        elif i == 4:
            mini_roman += "iv"
        elif i == 1:
            mini_roman += "i"
    return mini_roman.lower()

