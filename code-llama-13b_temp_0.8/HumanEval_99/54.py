
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
    # if value is a string
    if isinstance(value, str):
        # convert it to a float
        value = float(value)
    # if value is not a string or a float
    if not isinstance(value, (str, float)):
        # raise an error
        raise TypeError("Invalid type")
    # if the value is greater than or equal to zero
    if value >= 0:
        # round it down (truncates decimals) and add 0.5
        value = int(value) + 0.5
        # convert the result to an integer
        return int(value)
    # otherwise (if the value is less than zero)
    else:
        # round it up (truncates decimals) and subtract 0.5
        value = int(value) - 0.5
        # convert the result to an integer
        return int(value)
