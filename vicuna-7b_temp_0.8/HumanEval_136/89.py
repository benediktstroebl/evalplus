
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
    positive_lst = [x for x in lst if x > 0]
    negative_lst = [x for x in lst if x < 0]
    if positive_lst:
        max_pos = max(positive_lst)
        min_pos = min(positive_lst)
    else:
        max_pos = None
        min_pos = None
    if negative_lst:
        max_neg = max(negative_lst)
        min_neg = min(negative_lst)
    else:
        max_neg = None
        min_neg = None
    return max_pos, min_pos
