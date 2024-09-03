def closest_integer(value):
    '''
    Returns the closest integer to the given value, rounding away from zero
    if the number is equidistant from two integers.
    '''
    num = round(float(value))
    if abs(num - int(value)) == 0.5:
        return max(num, int(value))
    return int(value)