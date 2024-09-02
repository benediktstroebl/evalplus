
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
    for x in lst:
        if x < 0:
            neg_ints.append(x)
        else:
            pos_ints.append(x)

    if neg_ints == []:
        return (None, None)
    else:
        return (min(neg_ints), max(pos_ints))
