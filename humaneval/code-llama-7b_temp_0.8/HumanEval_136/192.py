
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
        if lst[0] >= 0:
            return None, lst[0]
        else:
            return lst[0], None
    else:
        lst.sort()
        neg = []
        pos = []
        for i in lst:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        if len(neg) == 0:
            return None, pos[0]
        elif len(pos) == 0:
            return neg[-1], None
        return neg[-1], pos[0]

