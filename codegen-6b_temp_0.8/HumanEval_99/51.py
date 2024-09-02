
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
    float_val = float(value)

    if float_val == int(float_val):
        return int(float_val)

    left = 0
    right = 10
    while right - left > 1:
        mid = (right + left) // 2

        if float_val > mid:
            left = mid

        if float_val < mid:
            right = mid

    if abs(float_val - left) < abs(float_val - right):
        return left

    return right

