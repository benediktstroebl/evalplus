
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

    roman_to_int = {
        "i": 1,
        "v": 5,
        "x": 10,
        "l": 50,
        "c": 100,
        "d": 500,
        "m": 1000,
    }
    result = []
    while number > 0:
        if number >= 1000:
            result.append("m")
            number -= 1000
        elif number >= 500:
            result.append("d")
            number -= 500
        elif number >= 100:
            result.append("c")
            number -= 100
        elif number >= 50:
            result.append("l")
            number -= 50
        elif number >= 10:
            result.append("x")
            number -= 10
        elif number >= 5:
            result.append("v")
            number -= 5
        elif number >= 1:
            result.append("i")
