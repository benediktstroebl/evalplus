
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
        int_value = int(float(value))
    except ValueError:
        int_value = None

    if int_value is None:
        return None

    value = abs(int_value)
    best_value = -1
    for i in range(1,value):
        if (value - i) % 2 == 0:
            if ((value - i) / 2) % 1 == 0:
                if i > best_value:
                    best_value = i
            else:
                best_value = i
        else:
            if ((value + i) / 2) % 1 == 0:
                if i > best_value:
                    best_value = -i
            else:
                best_value = -i

    return int_value + best_value
