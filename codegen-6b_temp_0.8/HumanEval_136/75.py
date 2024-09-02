
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
    num_neg = None
    num_pos = None
    for x in lst:
        if x < 0:
            if num_neg is None:
                num_neg = x
            else:
                if num_neg > x:
                    num_neg = x
        else:
            if num_pos is None:
                num_pos = x
            else:
                if num_pos < x:
                    num_pos = x
    return (num_neg, num_pos)

