
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
    neg_lst = [n for n in lst if n < 0]
    pos_lst = [n for n in lst if n > 0]
    if len(neg_lst) == 0 and len(pos_lst) == 0:
        return None, None
    if len(neg_lst) > 0:
        largest_neg = max(neg_lst)
        smallest_neg = neg_lst[0]
    else:
        largest_neg = float('-inf')
        smallest_neg = 0
    if len(pos_lst) > 0:
        largest_pos = min(pos_lst)
        smallest_pos = max(pos_lst)
    else:
        largest_pos = float('inf')
        smallest_pos = 1
    return largest_neg, smallest_pos