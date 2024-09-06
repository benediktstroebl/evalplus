
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
    # Use float representation of value to get the decimal and integer parts
    parts = value.as_float().split('.')
    whole_part, decimal_part = parts[0], parts[1]

    # Find the closest integer
    if decimal_part == '0':
        return int(whole_part)
    else:
        return int(whole_part) + 1
