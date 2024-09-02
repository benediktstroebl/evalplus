
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
    if lst:
        neg = pos = None
        for i in lst:
            if neg is None and i < 0:
                neg = i
            if pos is None and i > 0:
                pos = i
            if neg is not None and i > neg:
                neg = i
            if pos is not None and i < pos:
                pos = i
        return neg, pos
    return None, None

