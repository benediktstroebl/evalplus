
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

    largest_negative = None
    smallest_positive = None
    for num in lst:
        if largest_negative is None and num < 0:
            largest_negative = num
        elif largest_negative is not None and num < largest_negative and num < 0:
            largest_negative = num
        if smallest_positive is None and num > 0:
            smallest_positive = num
        elif smallest_positive is not None and num < smallest_positive and num > 0:
            smallest_positive = num
    return largest_negative, smallest_positive

