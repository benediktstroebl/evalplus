
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

    # My solution
    # if '.' not in value:
    #     return int(value)
    # if '.' in value:
    #     v = value.split('.')
    #     x = int(v[0])
    #     y = float('0.' + v[1])
    #     if round(y) == 0.5:
    #         if x < 0:
    #             return x - 1
    #         if x > 0:
    #             return x + 1
    #     if round(y) != 0.5:
    #         return round(float(value))

    # Clever solution
    import math

    num = float(value)
    round_towards_zero = int(num)
    round_away_from_zero = math.copysign(round(abs(num)), num)

    if abs(num - round_towards_zero) > abs(num - round_away_from_zero):
        return round_away_from_zero

    return round_towards_zero
