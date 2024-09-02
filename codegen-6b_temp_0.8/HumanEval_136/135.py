
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
    a = []
    b = []
    for x in lst:
        if x < 0:
            a.append(x)
        if x > 0:
            b.append(x)
    if len(a) == 0:
        a = None
    if len(b) == 0:
        b = None
    return (a, b)

