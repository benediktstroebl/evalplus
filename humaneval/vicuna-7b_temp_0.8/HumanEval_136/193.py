
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
        return None, None
    if lst[0] < 0:
        return (max(lst), -1)
    if lst[-1] > 0:
        return (-1, min(lst))
    for i in range(len(lst)-1):
        if lst[i] < 0:
            return (max(lst[0], max(lst[i+1])), -1)
        if lst[i] > 0:
            return (-1, min(lst[i], min(lst[i+1])))
    return (max(lst[0], max(lst[-1])), min(lst))
