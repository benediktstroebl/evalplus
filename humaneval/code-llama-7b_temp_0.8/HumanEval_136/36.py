
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
    neg_int = []
    pos_int = []
    for i in lst:
        if i < 0:
            neg_int.append(i)
        elif i > 0:
            pos_int.append(i)
        else:
            pass

    if neg_int != []:
        neg = max(neg_int)
    else:
        neg = None

    if pos_int != []:
        pos = min(pos_int)
    else:
        pos = None

    return(neg, pos)

