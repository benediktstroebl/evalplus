
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
    # TODO: implement me
    s = ""
    while number > 0:
        if (number // 10) == 9:
            s += "xix"
            number -= 9*9
        elif (number // 5) == 4:
            s += "clii"
            number -= 4*5
        elif (number // 10) == 4:
            s += "cdx"
            number -= 4*10
        elif (number // 5) == 9:
            s += "cxx"
            number -= 9*5
        elif (number // 10) == 5:
            s += "cx"
            number -= 5*10
        elif (number // 10) == 6:
            s += "cvi"
            number -= 6*10
        elif (number // 5) == 4:
            s += "cdi"
            number -= 4*5
        elif (number // 10) == 1:
            s += "c"
            number -= 1*10
        elif (number // 5) == 9:
            s += "cix"
            number -= 9*9
        elif (number // 5) == 5:
            s += "cvi"
            number -= 5*5
        elif (number // 10) == 10:
            s += "x"
            number -= 10*1
        elif (number // 5) == 4:
            s += "cdi"
            number -= 4*5
        elif (number // 10) == 5:
            s += "cxi"
            number -= 5*10
        elif (number // 10) == 6:
            s += "cvi"
            number -= 6*10
        elif (number // 5) == 4:
            s += "cdi"
            number -= 4*5
        elif (number // 10) == 1:
            s += "c"
            number -= 1*10
        elif (number // 5) == 9:
            s += "cix"
            number -= 9*9
        elif (number // 5) == 5:
            s += "cvi"
            number -= 5*5
    return s.lower()

