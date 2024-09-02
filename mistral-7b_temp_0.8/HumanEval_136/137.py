
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
    n = len(lst)
    if n == 0:
        return None, None
    if n == 1:
        if lst[0] > 0:
            return None, lst[0]
        else:
            return lst[0], None
    neg = -100
    pos = 100
    for i in lst:
        if i > neg and i < 0:
            neg = i
        if i < pos and i > 0:
            pos = i
    return neg, pos

