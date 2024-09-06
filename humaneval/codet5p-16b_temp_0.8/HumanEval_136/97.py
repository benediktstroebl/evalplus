
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

    pos_max = None
    neg_max = None

    for i in lst:
        if pos_max is None or pos_max < i:
            pos_max = i
        if neg_max is None or neg_max > i:
            neg_max = i

    return (neg_max, pos_max)
