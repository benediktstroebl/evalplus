
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
    min_negative = None
    min_positive = None

    for i in lst:
        if i < 0:
            if min_negative is None or i > min_negative:
                min_negative = i
        elif min_positive is None or i < min_positive:
            min_positive = i

    if min_negative is None and min_positive is None:
        return None, None
    elif min_negative is None:
        return None, min_positive
    elif min_positive is None:
        return min_negative, None
    else:
        return min_negative, min_
