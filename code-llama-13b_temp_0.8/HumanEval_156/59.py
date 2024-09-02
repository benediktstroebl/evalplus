
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
    one_prefixes = {
        1000: "m",
        900: "cm",
        500: "d",
        400: "cd",
        100: "c",
        90: "xc",
        50: "l",
        40: "xl",
        10: "x",
        9: "ix",
        5: "v",
        4: "iv",
        1: "i",
    }

    two_prefixes = {
        10: "x",
        9: "ix",
        5: "v",
        4: "iv",
    }

    two_place_nums = [
        10,
        9,
        5,
        4,
        1,
    ]

    roman_numeral = ""
    if number == 0:
        raise ValueError("No roman equivalent of zero")

    if number < 0:
        raise ValueError("Must be a positive integer")

    for num in two_place_nums:
        while number >= num:
            roman_numeral += two_prefixes[num]
            number -= num

    while number > 0:
        for n, r in one_prefixes.items():
            if number >= n:
                roman_numeral += r
                number -= n
                break

    return roman_numeral.lower()

