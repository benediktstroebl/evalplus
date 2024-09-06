
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
    # YOUR CODE HERE
    pos = None
    neg = None

    if len(lst) == 0:
        return None, None

    for x in lst:
        if x > 0:
            pos = x if pos is None else max(x, pos)
        elif x < 0:
            neg = x if neg is None else min(x, neg)

    return pos, neg
