
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
    # remove the fractional part
    value = value.rstrip('.')
    # remove trailing zeros
    value = value.rjust(2, '0')
    # calculate the number of digits
    n = len(value)
    # check if the number is negative
    if value[0] == '-':
        value = '-' + value[1:]
        n -= 1
    # find the closest integer
    for i in range(1, n + 1):
        # check if the number is equidistant from two integers
        if abs(value - i) < abs(value - i - 1) and abs(value - i) < abs(value - i + 1):
            # round it away from zero
            if value - i < 0:
                return i
            else:
                return i + 1
        else:
            if i - n/2 < 0:
                return i
    return 1000000000000000000