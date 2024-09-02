
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

    neg = 0
    pos = 0
    neg_largest = None
    pos_largest = None
    for x in lst:
        if x > 0:
            if pos == 0:
                pos_largest = x
            pos = 1
        elif x < 0:
            if neg == 0:
                neg_largest = x
            neg = 1
    if neg == 1:
        if neg_largest == None:
            return (None, None)
        else:
            return (neg_largest, None)
    elif pos == 1:
        if pos_largest == None:
            return (None, None)
        else:
            return (None, pos_largest)
    else:
        return (None, None)
