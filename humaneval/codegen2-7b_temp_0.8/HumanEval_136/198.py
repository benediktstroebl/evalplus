
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
    pos_list = []
    neg_list = []
    for num in lst:
        if num > 0:
            pos_list.append(num)
        elif num < 0:
            neg_list.append(num)

    if len(neg_list)!= 0:
        return (min(neg_list), None)
    elif len(pos_list)!= 0:
        return (None, max(pos_list))
    else:
        return (None, None)
