
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
    # Find the closest integer to the number given
    # If the number is equidistant from two integers, round it away from zero

    # Create a function that takes a value representing a number and returns the closest integer to it
    # If the number is equidistant from two integers, round it away from zero
    def find_closest_integer(number):
        closest_int = int(number)
        if number == str(closest_int):
            return number
        elif closest_int > int(number) > (closest_int-1):
            return str(closest_int)
        else:
            return str(closest_int-1)

    # Test the function
    print(find_closest_integer("10"))
    print(find_closest_integer("15.3"))
    print(find_closest_integer("14.5"))
    print(find_closest_integer("-14.5"))
