
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
    # 0.5 is equidistant from 0 and 1, but 1 is the further number away from zero
    # so we will take 1
    if value == "0.5":
        return 1
    # -0.5 is equidistance from -1 and 0, but -1 is the closer number to zero
    # so we will take -1
    if value == "-0.5":
        return -1

    # if the value is an integer
    # if the value is already a integer
    if value[0] == "-" or value[0] in list("1234567890"):
        return int(value)
    # if the value is a float
    else:
        # if the value is equidistant between two integers
        # then we will take the integer that is farther away from zero
        # for example 14.5 is equidistant between 14 and 15
        # so we will take 15
        if len(value.split(".")[1]) == 2:
            # if the first digit is 5 or greater
            if int(value.split(".")[1][0]) >= 5:
                return int(float(value)) + 1
            # if the first digit is 5 or lesser
            else:
                return int(float(value))
        # if the value is not equidistant between two integers
        else:
            return int(float(value))

