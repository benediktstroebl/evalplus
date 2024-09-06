
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
    for i in lst:
        if max_int == None and min_int == None:
            if i > 0:
                min_int = i
            elif i < 0:
                max_int = i
        else:
            if i > 0:
                if i >= max_int:
                    max_int = i
            elif i < 0:
                if i <= min_int:
                    min_int = i

    return (max_int, min_int)
    
