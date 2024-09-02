
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

    value_to_roman = {1: "i", 5: "v", 10: "x"}

    roman = []

    while number > 0:
        if number >= 400:
            roman.append("c")
            number -= 400
        elif number >= 100:
            roman.append("c")
            number -= 100
        elif number >= 50:
            roman.append("l")
            number -= 50
        elif number >= 10:
            roman.append("x")
            number -= 10
        elif number >= 5:
            roman.append("v")
            number -= 5
        elif number >= 1:
            roman.append("i")
            number -= 1

    return "".join(roman)
