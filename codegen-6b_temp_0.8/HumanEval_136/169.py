
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
    largest_negative, smallest_positive = None, None

    for x in lst:
        if x < 0:
            if largest_negative is None:
                largest_negative = x
            else:
                largest_negative = max(largest_negative, x)
        elif x > 0:
            if smallest_positive is None:
                smallest_positive = x
            else:
                smallest_positive = min(smallest_positive, x)
    return (largest_negative, smallest_positive)

