
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

    # The value is an integer, so return it
    if float(value) % 1 == 0:
        return float(value)
    
    # Get the difference between the float and the closest integer
    diff = abs(float(value) - round(float(value)))

    # Determine if it should round up or down
    if diff == 0.5:
        # If the float is equidistant from two integers, round it away from zero
        if float(value) > 0:
            return int(round(float(value)))
        else:
            return -int(round(float(value)))
    else:
        # Round to the closest integer
        return round(float(value))

