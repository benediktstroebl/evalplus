
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
    # smallest_pos = None
    # largest_neg = None
    # for x in lst:
    #     if smallest_pos is None or x < smallest_pos:
    #         smallest_pos = x
    #     if largest_neg is None or x > largest_neg:
    #         largest_neg = x
    #     if smallest_pos == 0 or largest_neg == 0:
    #         return None, None
    # return largest_neg, smallest_pos

    # reduce version
    from functools import reduce
    return reduce(lambda x, y: (x[0] if x[0] is not None and x[0] >= y else y,
                                x[1] if x[1] is not None and x[1] <= y else y),
                  lst, (None, None))

