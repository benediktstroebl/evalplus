
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
    _max, _min = None, None
    for i in lst:
        if type(i) == int and i < 0:
            _max = i if _max == None else max(_max, i)
        elif type(i) == int and i > 0:
            _min = i if _min == None else min(_min, i)
    return (_max, _min)

