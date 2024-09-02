
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
    pos_integers = []
    neg_integers = []
    for i in lst:
        if i >= 0:
            pos_integers.append(i)
        else:
            neg_integers.append(i)
    if len(pos_integers) == 0:
        return (None, None)
    elif len(neg_integers) == 0:
        return (None, None)
    else:
        return (min(neg_integers), max(pos_integers))

