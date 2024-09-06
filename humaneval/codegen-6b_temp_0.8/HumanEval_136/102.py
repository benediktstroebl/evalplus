
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
    lst1 = []
    for i in range(len(lst)):
        if lst[i] < 0:
            lst1.append(lst[i])
    lst1.sort()
    if len(lst1) == 0:
        a = None
        b = None
    else:
        a = lst1[-1]
        b = lst1[0]
    return (a, b)
