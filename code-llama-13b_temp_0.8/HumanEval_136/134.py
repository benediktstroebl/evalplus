
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

    min_positive = min_negative = None
    for el in lst:
        if el > 0:
            if min_positive is None or min_positive > el:
                min_positive = el
        if el < 0:
            if min_negative is None or min_negative > el:
                min_negative = el
    return (min_negative, min_positive)

