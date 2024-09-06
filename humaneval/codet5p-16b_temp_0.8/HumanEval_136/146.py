
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

    min_pos = None
    max_neg = None

    for x in lst:
        if x > 0:
            if min_pos is None:
                min_pos = x
            elif x < min_pos:
                min_pos = x
        elif x < 0:
            if max_neg is None:
                max_neg = x
            elif x > max_neg:
                max_neg = x
    return (max_neg, min_pos)
