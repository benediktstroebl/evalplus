
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
    neg_lst = [num for num in lst if num < 0]
    pos_lst = [num for num in lst if num > 0]
    if len(neg_lst) > len(pos_lst):
        return None, min(neg_lst)
    else:
        return max(neg_lst), max(pos_lst)
