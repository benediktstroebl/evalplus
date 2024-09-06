
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
    neg_ints = []
    pos_ints = []

    for i in lst:
        if i<0:
            neg_ints.append(i)
        elif i>0:
            pos_ints.append(i)

    if not neg_ints:
        return (None, None)

    if not pos_ints:
        return (neg_ints[0], None)

    return (max(neg_ints), min(pos_ints))
