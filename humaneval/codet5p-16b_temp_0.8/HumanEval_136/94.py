
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

    if len(lst) == 0:
        return (None, None)
    neg_lst = list(filter(lambda x: x < 0, lst))
    pos_lst = list(filter(lambda x: x > 0, lst))
    neg_lst = sorted(neg_lst, reverse=True)
    pos_lst = sorted(pos_lst, reverse=False)
    return (None, neg_lst[0]) if len(neg_lst) == 0 else (pos_lst[0], None)
    
    
    
