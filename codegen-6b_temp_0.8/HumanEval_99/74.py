
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
    import math
    
    if "." not in value:
        return int(value)
    
    numbers = [int(i) for i in value.split(".")]
    
    if len(numbers) == 1:
        return int(numbers[0])
    
    number = numbers[0]
    ind = 1
    
    if number > numbers[1]:
        number = numbers[1]
        ind = 0
    
    if number < numbers[1]:
        number = numbers[1]
        ind = 0
    
    if number == numbers[1]:
        if numbers[ind] == 0:
            return int(numbers[0])
        if numbers[ind] > 0:
            return int(numbers[0])
        
    
    '''
    if number > numbers[1]:
        number = numbers[1]
    
    if number < numbers[1]:
        number = numbers[1]
    '''
    
    base = math.ceil(number)
    
    if base == 0:
        base = 1
    
    if ind == 0:
        return base
    
    if base-number == 0:
        return base
    
    return base
    