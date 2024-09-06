
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

    # Workaround for differing behaviour on Python2 and Python3
    try:
        from math import isclose
    except ImportError:
        def isclose(a, b):
            return a == b

    try:
        from functools import reduce
    except ImportError:
        pass

    # Check that the input is numeric
    try:
        x = float(value)
    except ValueError:
        return

    # Find the integer that is closest to the input
    try:
        return reduce(lambda a, b: a if isclose(x, a) else b, range(int(x), int(x) + 1), -1)
    except NameError:
        return reduce(lambda a, b: a if isclose(x, a) else b, range(int(x), int(x) + 1), -1)
