
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
    def closest_integer(value):
        '''
        Use float to create decimal value from given string
        Use int to get modulo value from integer(returns closest)
        Use abs(x) to find the absolute value of the number
        Use round to round off the value
        '''
        decimal = float(value)
        return int(decimal - (decimal%1))
    return closest_integer(value)
