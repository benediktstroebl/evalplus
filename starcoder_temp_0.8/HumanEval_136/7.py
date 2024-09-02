
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
    l_neg = [item for item in lst if item < 0]
    l_pos = [item for item in lst if item > 0]
    if len(l_neg) == 0:
        neg = None
    else:
        neg = max(l_neg)
    if len(l_pos) == 0:
        pos = None
    else:
        pos = min(l_pos)
    return (neg, pos)
