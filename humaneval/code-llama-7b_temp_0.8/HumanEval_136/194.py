
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

    largest_negative_integer = None
    smallest_positive_integer = None
    for x in lst:
        if isinstance(x, int):
            if x < 0 and (not largest_negative_integer or largest_negative_integer < x):
                largest_negative_integer = x
            if x > 0 and (not smallest_positive_integer or smallest_positive_integer > x):
                smallest_positive_integer = x

    return (largest_negative_integer, smallest_positive_integer)
