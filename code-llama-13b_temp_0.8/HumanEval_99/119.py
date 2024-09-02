
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

    if "." in value:
        # if the value is a string, it has a .
        if len(value.split('.')[1]) == 1:
            # check to see if there is only 1 digit after the decimal
            return int(round(float(value)))
        else:
            # return the integer that is closest to the float value
            return int(value[::-1].replace(".", "", 1)[::-1])
    else:
        # if the value is an integer, return the value
        return int(value)

    # other solution
    if float(value) % 1 == 0:
        return int(value)
    return int(round(float(value)))
