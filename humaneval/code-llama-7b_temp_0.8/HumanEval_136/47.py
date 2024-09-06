
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
    min_pos, max_neg = None, None
    for i in lst:
        if type(i) == int:
            if i > 0:
                if min_pos is None or i < min_pos:
                    min_pos = i
            if i < 0:
                if max_neg is None or i > max_neg:
                    max_neg = i
    return max_neg, min_pos

