
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
    lg = sm = None
    for el in lst:
        if type(el) is not int:
            continue
        elif lg is None and el < 0:
            lg = el
        elif lg is not None and el < lg and el < 0:
            lg = el
        elif sm is None and el > 0:
            sm = el
        elif sm is not None and el > sm:
            sm = el
    return lg, sm

