def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000
    """
    if number == 1:
        return "i"
    elif number == 4:
        return "iv"
    elif number == 5:
        return "v"
    elif number == 9:
        return "ix"
    elif number == 10:
        return "x"
    elif number == 40:
        return "xl"
    elif number == 50:
        return "l"
    elif number == 90:
        return "xc"
    elif number == 100:
        return "c"
    elif number == 400:
        return "cd"
    elif number == 500:
        return "d"
    elif number == 900:
        return "cm"
    elif number == 1000:
        return "m"
    else:
        result = []
        for i in range(1000, number + 1, 200):
            result.append("c")
            result.append("x")
            result.append("l")
            result.append("i")
        result.reverse()
        return "".join(result)