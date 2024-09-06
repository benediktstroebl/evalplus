
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

    neg_num = []
    pos_num = []
    
    for num in lst:
        if num < 0:
            neg_num.append(num)
        else:
            pos_num.append(num)
    
    if len(neg_num) > len(pos_num):
        return (min(neg_num), None)
    elif len(neg_num) < len(pos_num):
        return (None, max(pos_num))
    else:
        return (None,
