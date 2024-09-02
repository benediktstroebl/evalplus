
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

    neg_list = [i for i in lst if i < 0]
    pos_list = [i for i in lst if i > 0]

    if len(neg_list) == 0:
        neg_list.append(None)
    if len(pos_list) == 0:
        pos_list.append(None)

    return (max(neg_list), min(pos_list))
