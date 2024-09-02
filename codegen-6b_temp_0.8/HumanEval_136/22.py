
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
    pos_num = max(lst, key=lambda x: isinstance(x, int))
    neg_num = None
    for i in lst:
        if isinstance(i, int):
            if i < 0:
                if neg_num is None or i < neg_num:
                    neg_num = i
                    continue
            if neg_num is None or i > neg_num:
                neg_num = i
    return (neg_num, pos_num)

