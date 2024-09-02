
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
    if not lst:
        return None, None

    max_negative = max(lst)
    min_positive = min(lst)

    if max_negative is not None and min_positive is not None:
        return max_negative, min_positive
    elif max_negative is None and min_positive is None:
        return None, None
    elif max_negative is not None and min_positive is not None:
        return max_negative, min_positive
    else:
        return None, None
