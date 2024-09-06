
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

    for x in lst:
        if x >= 0:
            if a == None:
                a = x
                b = x
            elif a < x:
                a = x
        else:
            if b == None:
                b = x
            elif b > x:
                b = x
    return (a, b)
    
