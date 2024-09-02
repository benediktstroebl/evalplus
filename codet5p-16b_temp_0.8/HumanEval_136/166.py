
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

    l = list(set(lst))
    l.sort()
    if len(l) == 0 or len(l) == 1:
        return (None, None)
    else:
        if l[0] < 0:
            a = l[-1]
        else:
            a = l[0]
        if l[-1] > 0:
            b = l[0]
        else:
            b = l[-1]
    return a, b
