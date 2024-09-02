
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
    # Handle strings that represent numbers
    if isinstance(value, str) and len(value) == 0:
        return 0
    if value.isdigit() and len(value) > 0:
        try:
            value = int(value)
            return round(value, 0)
        except ValueError:
            pass
    try:
        value = float(value)
        return round(value, 0)
    except ValueError:
        pass
    return round(value, 0)
