
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

    numbers = [int(x) for x in value]
    if len(numbers) == 1:
        return numbers[0]

    diff = abs(numbers[1] - numbers[0])
    for i in range(1, len(numbers)-1):
        if abs(numbers[i] - numbers[i-1]) < diff:
            continue
        diff = abs(numbers[i] - numbers[i-1])
        if abs(numbers[i+1] - numbers[i]) < diff:
            continue
        diff = abs(numbers[i+1] - numbers[i])
    
    return numbers[0] if numbers[0]!= 0 else numbers[1]
    
    
