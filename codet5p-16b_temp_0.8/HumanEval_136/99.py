
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
        return (None, None)

    max_int = None
    min_int = None
    for elem in lst:
        if max_int is None:
            max_int = elem

        if min_int is None:
            min_int = elem

        if elem < 0:
            max_int = elem
        else:
            min_int = elem

    return (max_int, min_int)
