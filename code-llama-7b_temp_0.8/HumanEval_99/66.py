
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
    if value.find('.') == -1:
        return value
    else:
        a = value.split('.')
        a0 = int(a[0])
        a1 = a[1]
        if len(a1) == 1:
            a1 = int(a[1])
            if a1 > 5:
                return a0 + 1
            else:
                return a0
        else:
            a1 = int(a[1][0])
            if a1 > 5:
                return a0 + 1
            else:
                return a0
