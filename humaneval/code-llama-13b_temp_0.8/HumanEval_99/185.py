
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
    # return int(value)
    # return int(round(float(value)))

    # # one liner
    # return int(round(float(value))) if abs(int(round(float(value))) - float(value)) > abs(int(value)) - float(value) else int(value)

    # # if-else
    # if abs(int(value) - float(value)) > abs(int(round(float(value))) - float(value)):
    #     return int(value)
    # return int(round(float(value)))

    # return the closest integer to the given number
    result = round(float(value))

    # check if result is equidistant from two integers
    # and if so, return the integer that is the farthest from zero
    return result if abs(result - float(value)) > abs(int(value) - float(value)) else int(value)
