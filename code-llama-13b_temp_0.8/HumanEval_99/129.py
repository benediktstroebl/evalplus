
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

    # code goes here
    if '.' not in value:
        return int(value)
    else:
        import decimal
        value = decimal.Decimal(value)
        ceil_value = int(value.to_integral(rounding=decimal.ROUND_CEILING))
        floor_value = int(value.to_integral(rounding=decimal.ROUND_FLOOR))
        if abs(value - decimal.Decimal(ceil_value)) < abs(value - decimal.Decimal(floor_value)):
            return ceil_value
        else:
            return floor_value

