
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

    # strips the string of all non numeric chars (including .)
    stripped_value = ''.join(char for char in value if char.isnumeric() or char == '.')
    # strips the string of all chars except for the decimal point
    stripped_value = stripped_value.replace('.', '')

    if len(stripped_value) > 0:
        # convert stripped string to int
        number = int(stripped_value)
        # convert int to float
        float_value = float(number)

        # compare value of value passed to this function to the value
        # of the float_value rounded down and up
        difference_down = value - round(float_value - 0.5, 0)
        difference_up = value - round(float_value + 0.5, 0)

        # if value of value passed to this function and value of the
        # float_value rounded down are equal, return value of the float_value rounded down
        if difference_down == 0:
            return round(float_value - 0.5, 0)
        # if value of value passed to this function and value of the
        # float_value rounded up are equal, return value of the float_value rounded up
        elif difference_up == 0:
            return round(float_value + 0.5, 0)
        # if value of value passed to this function and value of the
        # float_value rounded down are not equal, return value of the float_value rounded towards zero
        elif difference_down != 0:
            return round(float_value, 0)

