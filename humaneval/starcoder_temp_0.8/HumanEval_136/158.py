
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
        return (None, None)
    elif len(lst) == 1:
        if lst[0] >= 0:
            return (None, lst[0])
        else:
            return (lst[0], None)

    else:
        lis = [x for x in lst if x >= 0]
        lis2 = [x for x in lst if x < 0]
        lis3 = [x for x in lis2 if x <= max(lis)]
        if len(lis3) == 0:
            lis3 = max(lis2)
        else:
            lis3 = max(lis3)
        lis4 = [x for x in lis if x <= min(lis)]
        if len(lis4) == 0:
            lis4 = min(lis)
        else:
            lis4 = min(lis4)
        return (lis4, lis3)
