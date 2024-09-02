
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
    max_int = -999999999
    min_int = 999999999

    for i in lst:
        if i > max_int:
            max_int = i
        if i < min_int:
            min_int = i
    if max_int == -999999999 or min_int == 999999999:
        return (None, None)
    return (max_int, min_int
