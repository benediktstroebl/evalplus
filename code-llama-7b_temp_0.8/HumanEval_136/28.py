
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
    smallest_positive_integer = None
    largest_negative_integer = None
    for i in lst:
        if i < 0 and (largest_negative_integer is None or largest_negative_integer < i):
            largest_negative_integer = i

        if i > 0 and (smallest_positive_integer is None or smallest_positive_integer > i):
            smallest_positive_integer = i

    return (largest_negative_integer, smallest_positive_integer)
