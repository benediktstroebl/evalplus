
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


    # your code here
    # (also your tests)

    if value.isdigit() is False:
        return -1
    else:
        num = float(value)
        if num.is_integer() is True:
            return num
        elif num > 0:
            if num.is_integer() is False:
                num = int(num)
                num += 1
                return num
            else:
                return num
        else:
            if num.is_integer() is False:
                num = int(num)
                num -= 1
                return num
            else:
                return num




    # your code here



    # (also your tests)

