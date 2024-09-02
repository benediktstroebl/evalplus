
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
    if not isinstance(value, str):
        raise TypeError('Input should be a string')

    # Remove commas
    value = value.replace(',', '')

    try:
        int_value = int(value)
    except ValueError:
        return None

    if int_value % 1 == 0:
        return int_value
    elif int_value % 1 != 0:
        if int_value - int_value // 1 < 0.5:
            return int_value - int_value // 1
        else:
            return int_value - int_value // 1 + 1
