
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
    if len(lst) == 0:
        return None, None
    elif len(lst) == 1:
        if lst[0] > 0:
            return lst[0], None
        else:
            return None, lst[0]
    else:
        large = large_smallest_integers(lst[1:])[0]
        small = large_smallest_integers(lst[1:])[1]
        if lst[0] > 0 and large is not None and small is not None:
            return lst[0], small
        elif lst[0] < 0 and large is not None and small is not None:
            return large, lst[0]
        elif lst[0] > 0 and large is None and small is None:
            return lst[0], None
        elif lst[0] < 0 and large is None and small is None:
            return None, lst[0]
        else:
            return None, None
