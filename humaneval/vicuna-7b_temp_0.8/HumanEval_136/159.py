
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
    # check for negative and positive integers
    if sum([1 if i < 0 else 0 for i in lst]) > 0:
        # find largest negative and smallest positive integers
        max_neg = max([x for x in lst if x < 0])
        min_pos = min([x for x in lst if x > 0])
        # return tuple
        return (max_neg, min_pos) if max_neg > min_pos else (None, None)
    else:
        return (None, None)
