
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
    output = ""
    while number > 0:
        if number >= 1000:
            number -= 1000
            output += "m"
        elif number >= 900:
            number -= 900
            output += "cm"
        elif number >= 500:
            number -= 500
            output += "d"
        elif number >= 400:
            number -= 400
            output += "cd"
        elif number >= 100:
            number -= 100
            output += "c"
        elif number >= 90:
            number -= 90
            output += "xc"
        elif number >= 50:
            number -= 50
            output += "l"
        elif number >= 40:
            number -= 40
            output += "xl"
        elif number >= 10:
            number -= 10
            output += "x"
        elif number >= 9:
            number -= 9
            output += "ix"
        elif number >= 5:
            number -= 5
            output += "v"
        elif number >= 4:
            number -= 4
            output += "iv"
        elif number >= 1:
            number -= 1
            output += "i"
        else:
            raise ValueError("Only positive integers allowed")

    return output



