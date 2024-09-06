
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
    round_away_from_zero = lambda x, y: int(round((x+y)/2.0))

    integer_pairs = [(int(value), value)]

    for pair in integer_pairs:
        x, value = pair[0], pair[1]
        rounded = int(round(float(value)))

        if rounded > x:
            integer_pairs.append((rounded, value))

        if rounded < x:
            integer_pairs.append((rounded, value))

    return max(integer_pairs, key=lambda x: x[1])[0]

