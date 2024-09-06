
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
    # Try to get the number of digits after the decimal point
    try:
        decimal_places = value.count('.')
    except:
        # If it can't be parsed as a float, just return it as an int
        decimal_places = 0

    # Get the integer part of the value
    integer_part = int(value)

    # Get the floating point part of the value
    fp_part = float(value)

    # Check if the value is equal to an integer
    if integer_part == value:
        return integer_part

    # Check if the value is equal to the nearest integer
    if fp_part == int(fp_part) or abs(fp_part - int(fp_part)) <= abs(value - integer_part):
        return int(value)

    # Calculate the integer part of the value rounded to the correct number of decimals
    rounded_int = (integer_part + (decimal_places - 1) * fp_part) // fp_part

    # Round the integer part away from zero if needed
    rounded_int += int(round(rounded_int)) - 1

    return rounded_int
