
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
    # The following is only necessary to test the case of no integers at all
    if len(lst) == 0:
        return None, None

    # Initialize variables
    min_int = None
    max_int = None
    for i in lst:
        if i > 0 and (max_int is None or i < max_int):
            max_int = i
        elif i < 0 and (min_int is None or i > min_int):
            min_int = i
    return max_int, min_int
