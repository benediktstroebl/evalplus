
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
    lst_neg = filter(lambda x: x < 0, lst)
    lst_pos = filter(lambda x: x > 0, lst)

    if lst_neg:
        lst_neg_val = max(lst_neg)
    else:
        lst_neg_val = None

    if lst_pos:
        lst_pos_val = min(lst_pos)
    else:
        lst_pos_val = None

    return (lst_neg_val, lst_pos_val)
