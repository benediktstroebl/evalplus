
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
    # Using float(value) instead of int(value), and removing the % operator
    # would solve the problem, but wouldn't be the correct answer.
    #
    # The problem is that float(14.5) == float(14) == 14.0, and
    # float(-14.5) == float(-14) == -14.0.
    #
    # The answer is to round away from zero, and we do that by adding or
    # subtracting one:
    round_value = int(float(value) + 1) if value[0] == '-' else int(float(value) - 1)
    return round_value
