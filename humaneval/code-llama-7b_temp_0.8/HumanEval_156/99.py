
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
    # Use the official roman numerals:
    # https://en.wikipedia.org/wiki/Roman_numerals
    digits = [
        # digits >= 1000
        (1000, "m", ""),
        (500, "d", "cd"),
        (100, "c", "c"),
        (50, "l", "lxc"),
        (10, "x", "x"),
        (5, "v", "v"),
        (1, "i", "i"),
        # digits < 1000
        (100, "c", "c"),
        (10, "x", "x"),
        (5, "v", "v"),
        (1, "i", "i"),
    ]

    res = ""
    for x in digits:
        q, r, roman = x
        res += roman * (number // q)
        number %= q

    return res
