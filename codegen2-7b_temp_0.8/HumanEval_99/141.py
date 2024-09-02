
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
    closest_integer = 0
    difference = abs(float(value) - closest_integer)
    for i in range(1, abs(int(float(value))) + 1):
        if abs(i - int(float(value))) < difference:
            closest_integer = i
            difference = abs(i - int(float(value)))
    return int(float(value)) + closest_
