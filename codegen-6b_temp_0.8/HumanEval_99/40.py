
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
    if value == '0':
        return 0
    if value == '-0':
        return 0
    try:
        float_value = float(value)
    except:
        print("Error: Input must be a number.")
        return None
    # if value is an integer, just return it
    if float_value == int(float_value):
        return float_value

    # otherwise, find the closest integer
    for i in [-1, 1]:
        try:
            closest_number = int(float_value) + i
            if abs(float_value - closest_number) < abs(float_value - int(closest_number)):
                return closest_number
            else:
                return int(closest_number)
        except:
            pass
    return None
