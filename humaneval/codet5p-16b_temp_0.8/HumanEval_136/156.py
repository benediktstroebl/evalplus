
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

    max_neg, min_pos = None, None
    max_neg_lst, min_pos_lst = [], []

    for num in lst:
        if num < 0:
            max_neg_lst.append(num)
        elif num > 0:
            min_pos_lst.append(num)
        else:
            continue

    if max_neg_lst:
        max_neg = max(max_neg_lst)
    if min_pos_lst:
        min_pos = min(min_pos_lst)

    return (max_neg, min_pos)

