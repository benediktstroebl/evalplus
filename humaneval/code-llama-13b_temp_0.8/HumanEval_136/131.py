
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
    min_int = None
    max_int = None
    for el in lst:
        if isinstance(el, int):
            if el < 0:
                if a is None or el > a:
                    a = el
            if el >= 0:
                if b is None or el < b:
                    b = el
    if min_int is None and max_int is None:
        return (None, None)
    return (a, b)

