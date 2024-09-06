
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
    # Taking in absolute value of the value parameter and type casting to integer.
    val = int(abs(float(value)))
    # If the given number is equidistant,
    # checking if it is negative or positive and rounding it to the farthest integer.
    if val % 1 == 0.5:
        return int(val) if value[0] == '-' else -int(val)
    else:
        return round(val)

