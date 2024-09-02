
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
    negative_lst = []
    positive_lst = []
    for i in lst:
        if i < 0:
            negative_lst.append(i)
        elif i > 0:
            positive_lst.append(i)
    if negative_lst == []:
        return None, None
    else:
        return max(negative_lst), min(positive_lst)

    # Solution:
    # max_neg_val = max(negative_lst)
    # min_pos_val = min(positive_lst)
    # tuple_return = (max_neg_val, min_pos_val)
    # return tuple_return
