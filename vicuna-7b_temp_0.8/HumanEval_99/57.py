
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
    if value.isdigit() and len(str(value)) == 1:
        # If the number is only one digit and it's between 0-9
        return int(value)
    elif value.isdigit() and len(str(value)) == 2:
        # If the number is two digits and it's between 0-99
        if int(value) >= 100:
            return int(value)
        else:
            return int(value) - 100
    elif value.isalpha():
        # If the number is not a number (a string)
        return int(value.split(".")[0])
    else:
        return None
