
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''

    if value == "0":
        return "0"

    num = float(value)
    if num > 0:
        if int(num) == 0:
            return str(int(num))
        else:
            if num%1 == 0:
                return str(int(num))
            elif int(num) > 0 and num - int(num) >= 0.5:
                return str(int(num))
            elif int(num) > 0 and num - int(num) <= 0.5:
                return str(int(num) + 1)
            elif int(num) < 0 and num - int(num) <= 0.5:
                return str(int(num))
            elif int(num) < 0 and num - int(num) >= 0.5:
                return str(int(num) + 1)
    elif num < 0:
        if int(num) == 0:
            return str(int(num))
        else:
            if num%1 == 0
