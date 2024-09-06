
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
    numbers = [float(x) for x in value.split(".")]
    ans = None
    for n in numbers:
        if n not in (0, 0.0):
            if ans is None:
                ans = n
            diff = abs(n - ans)
            if diff > abs(ans - n):
                ans = n
    return round(ans)

