
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
    # Split string into integer and decimal parts
    integer = int(value[:value.find('.')])
    decimal = value[value.find('.')+1:]

    # If the integer part is 0, return it
    if integer == 0:
        return integer

    # If the integer part is not 0, convert decimal to integer
    # and determine which integer is closer
    decimal = float(decimal)
    if decimal < 0.5:
        return integer
    elif decimal >= 0.5:
        if value[0] == '-':
            return integer + 1
        elif value[0] != '-':
            return integer

