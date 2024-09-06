
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
    # NOTE: This function is also known as rounding to nearest integer
    # NOTE: The easiest way to solve this is to convert the given value to a float
    # NOTE: Then if the value is equidistant from two integers, round it away from zero
    # NOTE: Then convert the value back to an integer
    # NOTE: https://www.kite.com/python/answers/how-to-round-to-the-nearest-integer-in-python
    return int(round(float(value)))
