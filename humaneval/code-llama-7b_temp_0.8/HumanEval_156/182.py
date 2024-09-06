
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
    int_to_roman_dict = {
        1 : "i",
        4 : "iv",
        5 : "v",
        9 : "ix",
        10 : "x",
        40 : "xl",
        50 : "l",
        90 : "xc",
        100 : "c",
        400 : "cd",
        500 : "d",
        900 : "cm",
        1000 : "m"
    }
    result = ""

    while number > 0:
        if number in int_to_roman_dict:
            result += int_to_roman_dict[number]
            number -= number
        elif number >= 500:
            result += "d"
            number -= 500
        elif number >= 100:
            result += "c"
            number -= 100
        elif number >= 50:
            result += "l"
            number -= 50
        elif number >= 10:
            result += "x"
            number -= 10
        elif number >= 5:
            result += "v"
            number -= 5
        elif number >= 1:
            result += "i"
            number -= 1

    return result.lower()

