
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
    # Modify the values below this line
    value = float(value)
    nums = [float(str(num) + '.5') for num in range(int(value), int(value) + 10)]
    value = min(nums, key = lambda x: abs(x - value))
    # Modify the values above this line
    return int(value)

