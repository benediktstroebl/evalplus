
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

    # Round away from zero:
    #   If absolute difference between rounded and actual value is the same
    #   as the absolute difference between the values in question, pick
    #   the number closer to zero.
    #   If rounded value is closer to zero, pick that one.

    rounded = round(float(value))
    rounded_difference = abs(rounded - float(value))
    integer_difference = abs(int(value) - float(value))

    if rounded_difference == integer_difference:
        if int(value) > 0:
            return int(value) - 1
        else:
            return int(value) + 1
    else:
        return int(rounded)
