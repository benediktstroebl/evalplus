
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
    _lst = [x for x in lst if x > 0 or x < 0]
    if len(_lst) == 0:
        return (None, None)
    _lst.sort()
    a = None
    b = None
    if len(_lst) != 0:
        if _lst[0] < 0:
            a = _lst[0]
        if _lst[-1] > 0:
            b = _lst[-1]
        return (a, b)
