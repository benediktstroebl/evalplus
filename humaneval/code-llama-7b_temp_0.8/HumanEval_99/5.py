
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
    # This problem can be solved using simple data types and the
    # built-in functions abs(), round(), float(), str()
    float_value = float(value)
    rounded_value = round(float_value)
    if abs(float_value - rounded_value) == 0.5:
        if float_value > 0:
            rounded_value += 1
        else:
            rounded_value -= 1
    return int(str(rounded_value))
