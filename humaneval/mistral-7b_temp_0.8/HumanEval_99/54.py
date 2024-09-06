
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
    x = value.split('.')
    x[0] = int(x[0])
    x[1] = int(x[1])
    if x[0] == x[0] + x[1]:
        if x[1] < 5:
            return x[0]
        else:
            return x[0] + 1
    if x[1] <= 5:
        return x[0]
    else:
        return x[0] + 1
