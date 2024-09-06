
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

    # get the sign
    sign = value[0]
    # remove the sign
    value = value[1:]

    # the number is an integer
    if '.' not in value:
        return int(value)

    # split the number into integer and decimal
    # and remove the decimal
    int_part, decimal_part = value.split('.')
    decimal_part = decimal_part[:2]

    # the decimal is equal to '5'
    if decimal_part == '5':
        # if the integer is even, round it towards zero
        if int(int_part) % 2 == 0:
            int_part = int(int_part) - 1
        else:
            int_part = int(int_part) + 1
    # the decimal is smaller than '5'
    elif float(decimal_part) < 5:
        int_part = int(int_part)
    # the decimal is greater than '5'
    else:
        int_part = int(int_part) + 1

    # join the sign and the integer
    return int(sign + str(int_part))
