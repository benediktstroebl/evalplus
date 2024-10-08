
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
    pos_lst = [x for x in lst if x > 0]
    neg_lst = [x for x in lst if x < 0]
    if not pos_lst and not neg_lst:
        return (None, None)
    elif not pos_lst and neg_lst:
        return (None, min(neg_lst))
    elif not neg_lst and pos_lst:
        return (max(pos_lst), None)
    else:
        return (max(pos_lst), min(neg_lst))
