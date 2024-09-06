
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
    # code here
    # NOTE: "if" and "else" statements are being used for clarity.
    # You can solve this challenge without using if and else

    # NOTE 2: Float() is being used to compare the value given with its floored version
    # to determine if it is equidistant from two integers or not

    if value == float(value):
        return int(value)
    else:
        if round(float(value)) - float(value) == 0.5:
            return round(float(value)) if abs(round(float(value))) >= abs(float(value)) else round(float(value)) + 1
        else:
            return round(float(value))

