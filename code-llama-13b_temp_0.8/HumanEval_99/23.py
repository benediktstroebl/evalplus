
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

    # if number is equidistant from two integers, round it away from zero.
    # What if the number is equidistant from two integers, but one is 
    # negative and the other positive?

    # 1. takes a string, convert to number.
    # 2. take the intger value and round it.
    # 3. take the integer value and floor it.
    # 4. take the integer value and ceiling it.
    # 5. take the integer value and compare it to the rounded value.
    # 6. take the integer value and compare it to the floored value.
    # 7. take the integer value and compare it to the ceiling value.
    # 8. if the number is equidistant from two integers,
    # round it away from zero.
    # 9. convert the number to string and return it.

    # 1.
    value = int(value)
    # 2.
    rounded = round(value)
    # 3.
    floored = math.floor(value)
    # 4.
    ceiling = math.ceiling(value)
    # 5.
    rounded_diff = abs(rounded - value)
    floored_diff = abs(floored - value)
    ceiling_diff = abs(ceiling - value)
    # 8.
    if floored_diff == rounded_diff == ceiling_diff:
        if floored < 0:
            return ceiling
        elif ceiling < 0:
            return floored
        else:
            return rounded
    # 9.
    return str(rounded)

    # Alternative Solution
    #   val = int(float(value))
    #   equidistant = abs(val - int(float(value) + 0.5)) == 0.5
    #   return val if not equidistant or val < 0 else val + 1

    # Alternative Solution
    #   from math import copysign
    #   num = int(float(value))
    #   return num + int(copysign(1, num))
