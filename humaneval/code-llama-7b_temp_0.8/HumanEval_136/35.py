
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
        return None, None

    min_pos = None
    max_neg = None

    for i in lst:
        if max_neg is None and i < 0:
            max_neg = i
        elif max_neg is not None and i < max_neg:
            max_neg = i

        if min_pos is None and i > 0:
            min_pos = i
        elif min_pos is not None and i < min_pos:
            min_pos = i

    return max_neg, min_pos
