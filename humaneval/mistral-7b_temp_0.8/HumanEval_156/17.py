
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
    if number == 1000:
        return "m"
    else:
        if number == 900:
            return "cm"
        elif number == 500:
            return "d"
        elif number == 400:
            return "cd"
        elif number == 90:
            return "xc"
        elif number == 50:
            return "l"
        elif number == 40:
            return "xl"
        elif number == 10:
            return "x"
        else:
            return "i"

