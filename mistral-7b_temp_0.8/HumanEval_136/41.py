
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
    lst.sort()
    a = None
    b = None
    for i in range(len(lst)):
        if lst[i] < 0 and a is None:
            a = lst[i]
        elif lst[i] < 0:
            if a < lst[i]:
                a = lst[i]
        if lst[i] > 0 and b is None:
            b = lst[i]
        elif lst[i] > 0:
            if b > lst[i]:
                b = lst[i]
    return a, b


