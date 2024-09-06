
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

    a = None
    b = None

    for i in lst:
        if i < 0 and a is None:
            a = i
        elif i > 0 and b is None:
            b = i
        elif i < 0 and a is not None:
            b = i if b is None else min(a, b, i)
        elif i > 0 and b is not None:
            a = i if a is None else max(a, b, i)
        else:
            a = i if a is None else i
            b = i if b is None else i

    return (a, b)

