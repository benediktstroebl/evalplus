
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

    if lst == []:
        return (None, None)
    a = None
    b = None
    for i in lst:
        if a == None:
            if i > 0:
                a = i
                b = i
            else:
                continue
        elif a > 0:
            if i > 0:
                a = i
            elif i < a:
                a = i
        elif a < 0:
            if i < a:
                a = i
            elif i > a:
                a = i
    return (a, b)
