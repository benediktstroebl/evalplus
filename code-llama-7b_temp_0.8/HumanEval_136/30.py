
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
        return None, None
    
    lst_neg = []
    lst_pos = []
    
    for i in lst:
        if i < 0:
            lst_neg.append(i)
        elif i > 0:
            lst_pos.append(i)
            
    if len(lst_neg) > 0:
        neg_max = max(lst_neg)
    else:
        neg_max = None
        
    if len(lst_pos) > 0:
        pos_min = min(lst_pos)
    else:
        pos_min = None
    
    return neg_max, pos_min

