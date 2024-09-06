
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
    max_pos_num = max(lst)
    max_neg_num = max(map(abs,lst)) if any(x >= 0 for x in lst) else None
    return (max_neg_num if max_neg_num != None else max_pos_num, max_pos_num if max_pos_num != None else min(lst))
