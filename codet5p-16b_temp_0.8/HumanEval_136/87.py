
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

    neg_ints = [x for x in lst if x < 0]
    pos_ints = [x for x in lst if x > 0]

    if len(lst) == 0:
        return (None, None)
    elif len(neg_ints) == 0:
        return (None, None)
    elif len(pos_ints) == 0:
        return (None, None)
    elif len(neg_ints) == len(pos_ints):
        return (neg_ints[-1], pos_ints[0])
    elif len(neg_ints) > len(pos_ints):
        return (neg_ints[-1], None)
    else:
        return (pos_ints[0], None)
    pass

