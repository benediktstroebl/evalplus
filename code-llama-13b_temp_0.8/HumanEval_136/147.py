
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
    n_lst = [x for x in lst if x < 0]
    p_lst = [x for x in lst if x > 0]
    if not n_lst and not p_lst:
        return (None, None)
    elif not n_lst:
        return (None, p_lst[0])
    elif not p_lst:
        return (n_lst[-1], None)
    return (n_lst[-1], p_lst[0])

