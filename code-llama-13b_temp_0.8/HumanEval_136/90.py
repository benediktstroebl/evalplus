
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
    # Check for empty list
    if lst == []:
        return (None, None)
    # Find max negative integer
    neg_max = lst[0]
    if neg_max >= 0:
        neg_max = None
    else:
        for x in lst[1:]:
            if x > neg_max and x < 0:
                neg_max = x

    # Find min positive integer
    pos_min = lst[0]
    if pos_min < 0:
        pos_min = None
    else:
        for x in lst[1:]:
            if x < pos_min and x >= 0:
                pos_min = x

    return neg_max, pos_min

