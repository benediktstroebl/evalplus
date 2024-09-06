
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
    neg = lambda x: x < 0
    pos = lambda x: x > 0

    neg_lst = list(filter(neg, lst))
    pos_lst = list(filter(pos, lst))

    if neg_lst:
        neg_max = max(neg_lst)
        lst.remove(neg_max)
        return (neg_max, min(pos_lst))
    elif pos_lst:
        pos_min = min(pos_lst)
        lst.remove(pos_min)
        return (None, pos_min)
    else:
        return None, None
