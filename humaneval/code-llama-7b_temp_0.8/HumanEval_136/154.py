
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
    smallest_pos = None
    largest_neg = None
    
    for x in lst:
        if x < 0 and not smallest_pos:
            smallest_pos = x
        elif x > 0 and not largest_neg:
            largest_neg = x
        elif x < 0 and smallest_pos:
            if x < smallest_pos:
                smallest_pos = x
        elif x > 0 and largest_neg:
            if x > largest_neg:
                largest_neg = x
    
    return largest_neg, smallest_pos
