
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
    def _max_min(lst, reverse=False):
        '''
        A helper function that takes a list and returns the max/min number
        based on the reverse option.
        '''
        if any(i < 0 for i in lst) and not reverse:
            return None, None
        elif all(i > 0 for i in lst) and reverse:
            return None, None
        else:
            return max(lst, default=float('-inf')), min(lst, default=float('inf'))

    pos_lst = list(filter(lambda i: i > 0, lst))
    if pos_lst:
        return _max_min(pos_lst, reverse=True)

    neg_lst = list(filter(lambda i: i < 0, lst))
    if neg_lst:
        return _max_min(neg_lst, reverse=True)

    return None, None

