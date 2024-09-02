
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

    # 1. Convert to a float to keep the decimals
    # 2. Check if it's negative
    # 3. Add 0.5 to negative to round up
    # 4. Subtract 0.5 from positive to round up
    # 5. Convert to an integer
    # 6. Return
    return int(float(value) + (1 if float(value) < 0 else -1) * 0.5)
