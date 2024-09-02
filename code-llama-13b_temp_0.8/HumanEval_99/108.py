
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

    # 1. Convert string to number using int() or float()
    # 2. Use math.floor() or math.ceil() to find closest integer
    #    NOTE: if the number is equidistant to two integers,
    #          math.ceil() returns the integer that is further away from zero
    # 3. Check if the closest integer is equal to the original number.
    #    If it is, return the original number (because we were asked to
    #    round away from zero).
    #    If not, return the closest integer.

    try:
        value = int(value)
    except ValueError:
        value = float(value)

    from math import ceil, floor

    if ceil(value) == floor(value):
        return value

    if value < 0:
        return ceil(value)

    return floor(value)

