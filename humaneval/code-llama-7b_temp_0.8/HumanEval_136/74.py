
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
    largest_int = None
    smallest_int = None
    for item in lst:
        if item < 0:
            if largest_int is None:
                largest_int = item
            elif largest_int < item:
                largest_int = item
        elif item > 0:
            if smallest_int is None:
                smallest_int = item
            elif smallest_int > item:
                smallest_int = item
    return largest_int, smallest_int

