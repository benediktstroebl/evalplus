
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
    try:
        value = float(value)
        n = int(value)
        difference = abs(n - value)
        if difference == 0.0:
            return 1000000000
        elif difference <= 0.5:
            return n + 0.5
        elif difference <= 1.5:
            return n + 1.5
        elif difference <= 2.5:
            return n + 2.5
        else:
            return n + 3.5
    except ValueError:
        return 0
