
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
    lst = [abs(i) for i in lst]
    lst = sorted(lst)
    if lst[0] >= 0:
        a = lst[0]
    else:
        a = None
    if lst[-1] <= 0:
        b = lst[-1]
    else:
        b = None
    return (a, b
