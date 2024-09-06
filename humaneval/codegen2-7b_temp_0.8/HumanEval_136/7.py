
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
    a_max = b_min = None
    for x in lst:
        if x < 0:
            if a_max == None or x > a_max:
                a_max = x
            if b_min == None or x < b_min:
                b_min = x
    if a_max == None:
        a_max = None
    if b_min == None:
        b_min = None
    return (a_max, b_min)
