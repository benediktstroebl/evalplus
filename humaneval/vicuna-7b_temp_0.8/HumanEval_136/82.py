
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
    neg_lst = [i for i in lst if i < 0]
    pos_lst = [i for i in lst if i > 0]
    if not pos_lst and not neg_lst:
        return None, None
    if neg_lst:
        largest_neg = max(neg_lst)
        smallest_neg = min(neg_lst)
    if pos_lst:
        largest_pos = max(pos_lst)
        smallest_pos = min(pos_lst)
    else:
        largest_pos = max(neg_lst)
        smallest_pos = min(neg_lst)
    return largest_neg, smallest_pos
