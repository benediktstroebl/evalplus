
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

    lst = [i for i in lst if isinstance(i, int)]
    if len(lst) == 0:
        return None, None

    neg = min(i for i in lst if i < 0)
    pos = max(i for i in lst if i > 0)

    if neg == None and pos == None:
        return None, None

    if neg == None:
        return None, pos

    if pos == None:
        return neg, None

    return neg, pos
