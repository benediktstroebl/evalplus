
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

    smallest_positive = None
    largest_negative = None
    for x in lst:
        if isinstance(x, int) and x >= 0:
            if smallest_positive is None:
                smallest_positive = x
            elif x < smallest_positive:
                smallest_positive = x
        elif isinstance(x, int) and x <= 0:
            if largest_negative is None:
                largest_negative = x
            elif x > largest_negative:
                largest_negative = x
        else:
            pass
    return largest_negative, smallest_positive

