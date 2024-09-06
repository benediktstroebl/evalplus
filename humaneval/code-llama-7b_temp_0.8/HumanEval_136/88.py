
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
    # return (max([i for i in lst if i < 0]), min([i for i in lst if i > 0]))
    neg_int, pos_int = None, None
    for i in lst:
        if i < 0:
            if neg_int == None:
                neg_int = i
            else:
                neg_int = i if i > neg_int else neg_int
        elif i > 0:
            if pos_int == None:
                pos_int = i
            else:
                pos_int = i if i < pos_int else pos_int
    return (neg_int, pos_int)
