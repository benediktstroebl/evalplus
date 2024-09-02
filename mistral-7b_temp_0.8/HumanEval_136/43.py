
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
    pos = []
    neg = []
    for i in lst:
        if i >= 0:
            pos.append(i)
        if i < 0:
            neg.append(i)

    if not pos:
        return None,None
    if not neg:
        return None,None

    p_max = max(pos)
    n_min = min(neg)
    return p_max, n_min
