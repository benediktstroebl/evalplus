
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
    neg = []
    pos = []
    neg_max = None
    pos_min = None
    for i in lst:
        if i < 0:
            neg.append(i)
            neg_max = max(neg)
        if i > 0:
            pos.append(i)
            pos_min = min(pos)

    if neg_max == None and pos_min == None:
        return (None, None)
    else:
        return (neg_max, pos_min)
