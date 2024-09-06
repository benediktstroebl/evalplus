
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

    # truncate the value
    value = int(value)

    # check if the integer is even or odd
    if value % 2 == 0:
        # if even and greater than zero, decrement
        if value > 0:
            value -= 1
        # if even and less than zero, increment
        else:
            value += 1
    else:
        # if odd and greater than zero, increment
        if value > 0:
            value += 1
        # if odd and less than zero, decrement
        else:
            value -= 1

    return value
