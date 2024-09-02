
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
    # Code here
    from math import floor, ceil
    
    if float(value) % 1 == 0:
        return int(value)
    
    else:
        # check sign
        if value[0] == '-':
            # abs value
            value = float(value[1:])
            # check closest
            if value - floor(value) < ceil(value) - value:
                return int(floor(value))
            else:
                return int(ceil(value))
            
        else:
            value = float(value)
            # check closest
            if value - floor(value) < ceil(value) - value:
                return int(floor(value))
            else:
                return int(ceil(value))

