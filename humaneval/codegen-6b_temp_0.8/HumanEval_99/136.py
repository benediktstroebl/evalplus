
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
    # Warning: This is a naive implementation.
    value = float(value)
    min_diff = 1 << 31
    closest = 0
    for num in (int(value), int(value-1)): # keep ints
        diff = abs(value-num)
        if diff < min_diff:
            min_diff = diff
            closest = num
    if min_diff == 1:
        return closest
    else:
        return int(closest-1)

