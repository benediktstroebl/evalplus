
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
    if type(value) == str:
        if value.replace(".", "", 1).isdigit():
            value = float(value)
        else:
            return "Number must be a decimal number"
    elif type(value) == float:
        value = float(value)
    if type(value) != float:
        return False
    else:
        if value >= 0:
            if int(value) == value:
                return value
            else:
                return value + 1
        else:
            if int(value) == value:
                return value
            else:
                return value - 1

