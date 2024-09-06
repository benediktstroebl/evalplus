
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
    int_min = None
    int_max = None

    for num in lst:
        if num < 0:
            if int_max is None:
                int_max = num
            if int_min is None:
                int_min = num
        else:
            if int_max is None and num > 0:
                int_max = num
            if int_min is None and num < 0:
                int_min = num

    return int_max, int_min

