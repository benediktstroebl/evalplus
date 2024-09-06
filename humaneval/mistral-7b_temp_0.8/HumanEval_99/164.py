
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
    if type(value) is not str:
        return None
    if value == "0":
        return 0
    else:
        num = 0
        if value[0] == "-":
            for i in range(1, len(value)):
                num = num * 10 + int(value[i])
            return num - 1
        else:
            for i in range(0, len(value)):
                num = num * 10 + int(value[i])
            return num

