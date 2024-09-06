
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
    # Use a regex to match the number, the point, and the power
    match = re.search(r'([0-9]+(\.[0-9]+)?)(e-[0-9]+)?', value)
    if match:
        # If the match is successful, we have the number and the point
        if match.group(2):
            # If there is a point, use it to get the integer
            integer = int(match.group(1)) * pow(10, float(match.group(4)))
        else:
            # If there is no point, the number is already an integer
            integer = int(match.group(1))
    else:
        # If the match fails, return the original value
        return value
