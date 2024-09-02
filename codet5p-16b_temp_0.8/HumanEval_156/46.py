
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

    result = ""
    while number > 0:
        if number >= 1000:
            result += "m"
            number -= 1000
        elif number >= 900:
            result += "cm"
            number -= 900
        elif number >= 500:
            result += "d"
            number -= 500
        elif number >= 400:
            result += "cd"
            number -= 400
        elif number >= 100:
            result += "c"
            number -= 100
        elif number >= 90:
            result += "xc"
            number -= 90
        elif number >= 50:
            result += "l"
            number -= 50
        elif number >= 40:
            result += "xl"
            number -= 40
        elif number >= 10:
            result += "x"
            number -= 10
        elif number >= 9:
            result += "ix"
            number -= 9
        elif number >= 5:
            result += "v"
            number -= 5
        elif number >= 4:
            result += "iv"
            number -= 4
        elif number
