
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
    neg_min = None
    pos_max = None
    for n in lst:
        if n < 0:
            if neg_min is None or n > neg_min:
                neg_min = n
        if n > 0:
            if pos_max is None or n < pos_max:
                pos_max = n
    return (neg_min, pos_max)
