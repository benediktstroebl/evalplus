
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

    neg_list = [lst[i] for i in range(len(lst)) if lst[i] < 0]
    pos_list = [lst[i] for i in range(len(lst)) if lst[i] >= 0]

    if neg_list:
        neg_list.sort()
        neg_max = neg_list[-1]

    else:
        neg_max = None

    if pos_list:
        pos_list.sort()
        pos_min = pos_list[0]

    else:
        pos_min = None

    return (neg_max, pos_min)
