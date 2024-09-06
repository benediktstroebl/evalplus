
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
    l = []
    for i in lst:
        if i >= 0:
            l.append(i)
        else:
            pass
    try:
        a = max(l)
    except ValueError:
        a = None
    try:
        b = min(lst)
    except ValueError:
        b = None
    return a, b
