
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

    neg_num = 0
    pos_num = 0
    if lst == []:
        return (None, None)
    for x in lst:
        if x < 0:
            neg_num = x
        elif x > 0:
            pos_num = x
    if neg_num > pos_num:
        return (neg_num, None)
    elif pos_num > neg_num:
        return (None, pos_num)
    else:
        return (None, None)

