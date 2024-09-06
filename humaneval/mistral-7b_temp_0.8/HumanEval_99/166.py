
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

    if '.' in value:
        number = float(value)
        int_to_return = number
        whole = int(number)
        if whole < number:
            int_to_return = whole + 1
        elif whole > number:
            int_to_return = whole - 1
    else:
        int_to_return = value
    return int_to_return



































































































































































