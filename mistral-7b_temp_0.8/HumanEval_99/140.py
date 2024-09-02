
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
    # Use int() to convert the given value to an integer.
    # If you can't convert it, return the given value.
    # If you can convert it to an integer, find the closest integer
    # using the round() function.
    # If you get two integers, use math.copysign() to find the one
    # that is further from zero.
    # Return the result.
    return value if int(value) is not value else round(int(value))
    # math.copysign(value, 1 if value > 0 else -1)
