
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
    min_val = None
    max_val = None

    for val in lst:
        if (min_val is None) or (min_val > val and val < 0):
            min_val = val
        if (max_val is None) or (max_val < val and val > 0):
            max_val = val
    return min_val, max_val

