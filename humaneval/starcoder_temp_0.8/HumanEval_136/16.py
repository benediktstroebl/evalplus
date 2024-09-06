
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
    n = []
    for i in lst:
        if i > 0:
            n.append(i)
        if i < 0:
            p = i
    if len(n) > 0:
        n = max(n)
    else:
        n = None
    if len(p) > 0:
        p = min(p)
    else:
        p = None
    return (p, n)
