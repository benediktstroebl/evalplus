
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
    # Step 1: check if the value is integer
    if float(value) % 1 == 0:
        return int(value)
    
    # Step 2: round the value to the closest integer
    rounded = round(float(value))
    
    # Step 3: check the difference between the rounded value and the original
    if abs(float(value) - rounded) > 0.5:
        return rounded + 1 if float(value) > 0 else rounded - 1
    
    # Step 4: return the rounded value
    return rounded
    
