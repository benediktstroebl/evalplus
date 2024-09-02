
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
    n = len(lst)
    neg_lst = []
    pos_lst = []
    for i in range(n):
        if lst[i] < 0:
            neg_lst.append(lst[i])
        elif lst[i] > 0:
            pos_lst.append(lst[i])
        else:
            return None, None
    if len(pos_lst) == 0:
        return None, None
    elif len(neg_lst) == 0:
        return None, pos_lst[0]
    return max(neg_lst), min(pos_lst)

