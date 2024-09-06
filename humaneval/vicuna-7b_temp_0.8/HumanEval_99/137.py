
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
    # Convert the value to an integer
    value = int(value)

    # Find the largest integer less than or equal to the value
    largest = max(int(value) - 1, 0)

    # Find the smallest integer greater than or equal to the value
    smallest = min(value + 1, 10)

    # If the value is less than the smallest integer or greater than the
    # largest integer, return the closest integer as the smallest integer
    if value < smallest:
        return smallest
    elif value > largest:
        return largest

    # Otherwise, round the closest integer away from zero
    rounded = round(closest_integer(value))

    return rounded
