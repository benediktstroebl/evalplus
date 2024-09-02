
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
    
    # Find the smallest positive number in a list
    if len(lst) == 0:
        return None, None
    else:
        min_pos = 1000000
        for x in lst:
            if type(x) == int and x > 0:
                if x < min_pos:
                    min_pos = x
        if min_pos == 1000000:
            min_pos = None
        
    # Find the largest negative number in a list
    if len(lst) == 0:
        return None, None
    else:
        max_neg = -1000000
        for x in lst:
            if type(x) == int and x < 0:
                if x > max_neg:
                    max_neg = x
        if max_neg == -1000000:
            max_neg = None
        
    return max_neg, min_pos
