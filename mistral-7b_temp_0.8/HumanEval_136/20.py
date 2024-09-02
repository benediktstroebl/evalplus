
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
    neg_num = []
    pos_num = []
    for i in lst:
        if i > 0:
            pos_num.append(i)
        if i < 0:
            neg_num.append(i)
    if len(pos_num) > 0:
        pos = min(pos_num)
    else:
        pos = None
    if len(neg_num) > 0:
        neg = max(neg_num)
    else:
        neg = None
    return (neg, pos)



