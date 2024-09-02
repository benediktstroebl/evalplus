
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
    # your code here
    int_value = int(value)
    if int_value == 0:
        return int_value

    str_value = str(value)
    if "." in str_value:
        len_value = len(str_value.split('.')[1])
        if len_value < 3:
            return int(value)

    return int(math.copysign(int(abs(value) + 0.5), value))
