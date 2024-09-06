
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
    # Step 1:
    # check if the value is an integer
    # if it is, return the integer
    # else, convert to float

    # Step 2:
    # round to integer

    # Step 3:
    # if negative, subtract 1

    # Step 4:
    # if the abs difference from the integer is greater than 0.5,
    # add 1
    # return the integer

    # Step 5:
    # return the integer

    # def closest_integer(value):
    #     # Step 1:
    #     # check if the value is an integer
    #     # if it is, return the integer
    #     # else, convert to float
    #     if int(float(value)) == float(value):
    #         return int(float(value))
    #     else:
    #         value = float(value)

    #     # Step 2:
    #     # round to integer
    #     value = round(value)

    #     # Step 3:
    #     # if negative, subtract 1
    #     if value < 0:
    #         value -= 1

    #     # Step 4:
    #     # if the abs difference from the integer is greater than 0.5,
    #     # add 1
    #     if abs(value - float(value)) > 0.5:
    #         value += 1

    #     # Step 5:
    #     # return the integer
    #     return int(value)


    # One line solution:
    return round(float(value)) if int(float(value)) == float(value) else round(float(value) + cmp(value, 0))
