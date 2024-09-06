
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
    s = []
    for i in lst:
        if i < 0:
            l.append(i)
        elif i > 0:
            s.append(i)

    if len(l) > 0:
        l.sort()
        l.reverse()
        l = l[0]
    else:
        l = None

    if len(s) > 0:
        s.sort()
        s = s[0]
    else:
        s = None

    return (l, s)

