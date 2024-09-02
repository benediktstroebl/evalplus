
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
    lst = [abs(i) for i in lst]
    neg_indexes = [i for i, x in enumerate(lst) if x < 0]
    pos_indexes = [i for i, x in enumerate(lst) if x > 0]
    if len(neg_indexes) == 0:
        return (None, lst[0])
    else:
        return (lst[neg_indexes[-1]], lst[0])

