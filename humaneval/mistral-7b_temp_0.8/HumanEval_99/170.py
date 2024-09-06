
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
    # Your code here

    # Returns the integer closest to the given value
    def nearest_integer(value):
        if value % 1 == 0:
            return int(value)
        elif value > 0:
            return value + 1
        else:
            return value - 1

    # Returns the integer closest to the given value
    # that is the farthest from 0
    def nearest_integer_away_from_zero(value):
        if value % 1 == 0:
            if value > 0:
                return value + 1
            else:
                return value - 1
        else:
            if value > 0:
                return value + 1
            else:
                return value - 1

    # Takes a string representing a number and returns the closest integer
    # to it
    def closest_integer(value):
        integer = nearest_integer(value)

        if integer == nearest_integer_away_from_zero(value):
            return integer
        else:
            return nearest_integer_away_from
