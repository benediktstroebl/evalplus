
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
    min_pos = max_neg = None
    for i in lst:
        if i < 0:
            if min_neg is None:
                min_neg = i
            if i < min_neg:
                min_neg = i
        else:
            if i > 0 and max_neg is None:
                max_neg = i
            if i > 0 and i > max_neg:
                max_neg = i
    return max_neg, min_neg
