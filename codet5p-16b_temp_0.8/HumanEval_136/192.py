
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

    max_int = None
    min_int = None
    if len(lst) < 1:
        return None, None
    else:
        for x in lst:
            if x > 0:
                if max_int is None:
                    max_int = x
                if x > max_int:
                    max_int = x
            elif x < 0:
                if min_int is None:
                    min_int = x
                if x < min_int:
                    min_int = x
    return (min_int, max_int)
    
