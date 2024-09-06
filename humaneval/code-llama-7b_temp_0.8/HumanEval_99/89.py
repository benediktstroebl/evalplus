
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
    # convert input to float
    value = float(value)

    # calculate the ceiling, floor and round of the input
    ceil = int(value // 1)
    floor = ceil - 1
    round = int(value % 1 * 10)

    # check which value is closer to zero
    ceil_to_zero = abs(ceil)
    floor_to_zero = abs(floor)
    round_to_zero = abs(round)

    if ceil_to_zero <= round_to_zero and ceil_to_zero <= floor_to_zero:
        return ceil
    elif floor_to_zero <= round_to_zero and floor_to_zero <= ceil_to_zero:
        return floor
    elif round_to_zero < ceil_to_zero and round_to_zero < floor_to_zero:
        return round
