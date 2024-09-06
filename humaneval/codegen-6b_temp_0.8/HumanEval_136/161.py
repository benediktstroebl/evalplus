
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
    neg_lst = []
    pos_lst = []
    for num in lst:
        if num <= 0:
            neg_lst.append(num)
        else:
            pos_lst.append(num)
    if len(neg_lst) == 0:
        neg_lst = None
    elif len(neg_lst) == 1:
        neg_lst = neg_lst[0]
    else:
        neg_lst = min(neg_lst)

    if len(pos_lst) == 0:
        pos_lst = None
    elif len(pos_lst) == 1:
        pos_lst = pos_lst[0]
    else:
        pos_lst = max(pos_lst)

    #print(neg_lst, pos_lst)
    return (neg_lst, pos_lst)

