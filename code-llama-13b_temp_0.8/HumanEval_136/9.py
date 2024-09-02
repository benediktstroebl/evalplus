
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

    negs = []
    poss = []
    for i in lst:
        if i < 0:
            negs.append(i)
        elif i > 0:
            poss.append(i)
    if not negs and not poss:
        return (None, None)
    if not negs:
        return (None, min(poss))
    if not poss:
        return (max(negs), None)
    return (max(negs), min(poss))

