
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

    # Check that a string is passed into the function
    if not isinstance(value, str):
        raise TypeError('Value must be a string')

    # Check that the string value contains a number
    if not value.replace('.', '').isdigit():
        raise ValueError('Value must be a number')

    # Convert the string into a float
    value = float(value)

    # Check if the value is equidistant between two integers
    if value % 1 == 0.5:
        # Check if the value is positive or negative
        if value > 0:
            return value + 0.5
        else:
            return value - 0.5
    else:
        # Check if the value is equidistant between two integers
        if value % 1 == 0.5:
            # Check if the value is positive or negative
            if value > 0:
                return value + 0.5
            else:
                return value - 0.5
        else:
            return round(value)

