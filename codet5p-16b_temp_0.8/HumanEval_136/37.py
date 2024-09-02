
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

    neg = None
    pos = None
    for num in lst:
        if num < 0:
            if neg is None:
                neg = num
            elif num > neg:
                neg = num
        elif num > 0:
            if pos is None:
                pos = num
            elif num < pos:
                pos = num
    if neg is not None:
        neg = abs(neg)
    if pos is not None:
        pos = abs(pos)
    return (neg, pos)

