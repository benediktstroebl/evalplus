
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
    if len(lst) == 0:
        return (None, None)
    lst.sort()
    neg_int = lst.index(-1)
    pos_int = lst.index(1)
    if neg_int == 0:
        return (None, lst[pos_int])
    elif pos_int == len(lst) - 1:
        return (lst[neg_int], None)
    else:
        return (lst[neg_int], lst[pos_int +
