
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
    # Make a tuple of (a,b)
    if len(lst) == 0:
        return None, None
    if len(lst) == 1:
        return None, lst[0]

    # First check for negative integers
    # If there are none, return None for a
    # If there are positive integers, return smallest positive integer as a
    a = None
    b = None
    for integer in lst:
        if integer < 0:
            if a == None:
                a = integer
            elif integer > a:
                a = integer
        elif integer > 0:
            if b == None:
                b = integer
            elif integer < b:
                b = integer

    return a,b
