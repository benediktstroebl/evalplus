
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

    # Find the number to round, either positive or negative
    value_num = float(value)
    # Round that number to the nearest integer
    rounded = round(value_num)
    # If the rounded number is equal to the given number, return it
    if rounded == value_num:
        return rounded
    # Otherwise, check if the difference between the rounded number and
    # the given number is smaller than the difference between the rounded
    # number and the next integer
    elif abs(value_num - rounded) < abs(rounded - int(rounded + 1)):
        # If it is, return the rounded number
        return rounded
    # Otherwise, return the next integer
    else:
        return int(rounded + 1)


