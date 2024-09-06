
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
    if not lst:
        return (None, None)
    if not lst[0] in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return (None, lst[0])
    if not lst[-1] in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return (lst[-1], None)
    n = len(lst)
    for i in range(n-1):
        if lst[i] < 0:
            return (lst[i+1], -10**(len(lst)-i-1))
        if lst[i] > 0:
            return (-10**(len(lst)-i-1), lst[i])
    return (None, None)
