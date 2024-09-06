
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
    def round_away_from_zero(number):
        return int(math.floor(float(number)))
    if value.isdigit():
        return int(value)
    number = float(value)
    rounded = round_away_from_zero(number)
    diff = abs(rounded - number)
    if diff == 0:
        return rounded
    elif diff > 0:
        return rounded + 1
    else:
        return rounded -
