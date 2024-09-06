
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
    def recurse(curr, num):
        if curr == 4:
            return num + 'cd'
        elif curr == 9:
            return num + 'cm'
        elif curr == 40:
            return num + 'd'
        elif curr == 90:
            return num + 'l'
        elif curr == 400:
            return num + 'l' + recurse(curr - 400, num)
        elif curr == 900:
            return num + 'l' + recurse(curr - 900, num)
        elif curr == 400:
            return num + 'c' + recurse(curr - 400, num)
        elif curr == 900:
            return num + 'c' + recurse(curr - 900, num)
        elif curr == 500:
            return num + 'c' + recurse(curr - 500, num)
        elif curr == 1000:
            return num + 'c' + recurse(curr - 1000, num)
        elif curr > 1000:
            return ""
        elif curr < 4:
            return num + recurse(curr, num)
        elif curr < 9:
            return num + 'x' + recurse(curr, num)
        elif curr < 40:
            return num + 'l' + recurse(curr, num)
        elif curr < 90:
            return num + 'c' + recurse(curr, num)
        elif curr < 400:
            return num + 'd' + recurse(curr, num)
        elif curr < 900:
            return num + 'm' + recurse(curr, num)
        elif curr < 1000:
            return num + 'b' + recurse(curr, num)

    return recurse(number, '')

