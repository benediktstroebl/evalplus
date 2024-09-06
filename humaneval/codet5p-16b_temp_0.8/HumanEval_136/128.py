
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
        if a is None and b is None:
            if i < 0:
                a = i
                if i > 0:
                    b = i
            elif i > 0:
                b = i
        else:
            if i < 0:
                if a is None:
                    a = i
                elif i > a:
                    a = i
            elif i > 0:
                if b is None:
                    b = i
                elif i < b:
                    b = i
    return (a, b)

