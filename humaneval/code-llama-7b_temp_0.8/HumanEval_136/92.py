
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    min_integer, max_integer = None, None
    for value in lst:
        if isinstance(value, int):
            if value > 0:
                if max_integer == None or max_integer < value:
                    max_integer = value
            elif value < 0:
                if min_integer == None or min_integer > value:
                    min_integer = value

    return min_integer, max_integer
