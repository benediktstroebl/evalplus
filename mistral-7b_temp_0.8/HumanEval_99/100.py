
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
    result = float(value)

    # if the float is evenly divisible by 2, add .5
    if result % 1 == 0:
        result = result + .5

    # if the number is an integer, return that number
    if result % 1 == 0:
        return result

    # if the number is an integer plus .5, return the integer
    if result % 1 == .5:
        return int(result)

    # if the number is divisible by 2, round down
    if result % 2 == 0:
        return int(result - .5)

    # if the number is divisible by 2 plus .5, round up
    if result % 2 == .5:
        return int(result + .5)
