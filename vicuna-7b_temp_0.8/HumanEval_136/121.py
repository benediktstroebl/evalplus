
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
    neg_lst = [x for x in lst if x < 0]
    pos_lst = [x for x in lst if x > 0]
    if neg_lst and pos_lst:
        max_lst = max(neg_lst + pos_lst)
        min_lst = min(neg_lst + pos_lst)
        return max_lst, min_lst
    elif neg_lst:
        return max(-neg_lst[0], -neg_lst[1]), min(-neg_lst[0], -neg_lst[1])
    elif pos_lst:
        return max(pos_lst[0], pos_lst[1]), min(pos_lst[0], pos_lst[1])
    else:
        return None, None

result = largest_smallest_integers([3, 5, 1, 4, 2, 7])
