
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
    max_neg = min_pos = None
    for n in lst:
        if n < 0 and max_neg is None or max_neg < n:
            max_neg = n
        elif n > 0 and min_pos is None or min_pos > n:
            min_pos = n

    return max_neg, min_pos

