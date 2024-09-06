
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

    # 1. Create two variables, one to store the floating value, the other an integer
    # 2. Use the float() method to convert the string to a float
    # 3. Use the round() method to round it to the nearest integer
    # 4. Use the int() method to convert it back to an integer
    # 5. Return the result

    # MY SOLUTION
    # f_val = float(value)
    # i_val = int(round(f_val))

    # if f_val == i_val:
    #   return i_val

    # else:
    #   if abs(f_val) - abs(i_val) > 0.5:
    #     return int(f_val) + 1 if f_val > 0 else int(f_val) - 1

    #   else:
    #     return i_val

    # SOLUTION 2
    from math import floor, ceil
    if (ceil(float(value)) - float(value)) > (float(value) - floor(float(value))):
      return int(ceil(float(value)))
    else:
      return int(floor(float(value)))

    # SOLUTION 3
    # import math

    # def closest_integer(value):
    #   if (abs(float(value) - math.floor(float(value))) > abs(float(value) - math.ceil(float(value)))):
    #     return int(math.ceil(float(value)))
    #   else:
    #     return int(math.floor(float(value)))



    # SOLUTION 4
    # def closest_integer(value):
    #   value = int(float(value))
    #   return value if float(value) == float(value) else value + 1 if value >= 0 else value - 1


    # SOLUTION 5
    # def closest_integer(value):
    #   if float(value) - int(value) > 0.5:
    #     return int(float(value) + 0.9
