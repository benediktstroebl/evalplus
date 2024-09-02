
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
    n = int(value)
    delta = abs(value - n)
    while True:
        i = n // 10
        if i == n:
            return n
        else:
            n = i * 10
            if delta < 0:
                delta = abs(delta)
            elif delta > 0:
                delta = -delta
    return n
