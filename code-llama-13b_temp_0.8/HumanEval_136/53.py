
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
    l_neg = None
    s_pos = None
    for x in lst:
        if x < 0 and (l_neg is None or x < l_neg):
            l_neg = x
        if x >= 0 and (s_pos is None or x > s_pos):
            s_pos = x
    return l_neg, s_pos

