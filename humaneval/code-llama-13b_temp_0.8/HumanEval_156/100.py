
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
    # Dictionary
    d = {
        1: "i",
        4: "iv",
        5: "v",
        9: "ix",
        10: "x",
        40: "xl",
        50: "l",
        90: "xc",
        100: "c",
        400: "cd",
        500: "d",
        900: "cm",
        1000: "m",
    }

    # Output
    s = ""

    # Initialization
    # 400, 900, 90, 40, 9, 4, 1
    keys = [1000, 900, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    # Loop
    while number > 0:
        for key in keys:
            while number >= key:
                number -= key
                s += d[key]

    return s
