
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

    pos = [n for n in lst if n > 0]
    neg = [n for n in lst if n < 0]
    pos.sort()
    neg.sort()
    if len(neg) == 0:
        return (None, None)
    if len(pos) == 0:
        return (None, None)
    return (neg[-1], pos[0])
