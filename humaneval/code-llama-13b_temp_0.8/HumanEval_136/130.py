
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
    neg_lst = []
    pos_lst = []
    for x in lst:
        if x < 0:
            neg_lst.append(x)
        if x >= 0:
            pos_lst.append(x)
    if len(neg_lst) > 0:
        neg_smallest = min(neg_lst)
    else:
        neg_smallest = None
    if len(pos_lst) > 0:
        pos_largest = max(pos_lst)
    else:
        pos_largest = None
    return neg_smallest, pos_largest

