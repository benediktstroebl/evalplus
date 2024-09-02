
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
    if len(lst) == 1 and lst[0] < 0:
        return (lst[0], None)
    if len(lst) == 1 and lst[0] >= 0:
        return (None, lst[0])
    largest_neg = None
    smallest_pos = None
    lst.sort()
    for i in range(len(lst) - 1):
        if lst[i] < 0:
            largest_neg = lst[i]
        elif lst[i] > 0:
            smallest_pos = lst[i]
    return (largest_neg, smallest_pos)

