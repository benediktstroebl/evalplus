
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
    n_max = n_min = None
    for i in lst:
        if i > n_max:
            n_max = i
        elif i < n_min:
            n_min = i
    n_max, n_min = (n_max, n_min) if n_max is not None or n_min is not None else (None, None)
    return (n_max, n_min)


