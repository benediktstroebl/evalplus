
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
    # My Code
    # max_neg = min_pos = None
    # for i in lst:
    #     if i < 0 and not max_neg or max_neg < i:
    #         max_neg = i
    #     if i > 0 and not min_pos or min_pos > i:
    #         min_pos = i
    # return max_neg, min_pos

    # Igor's Solution
    max_neg = min_pos = None
    for i in lst:
        if i < 0:
            max_neg = max(max_neg, i) if max_neg else i
        elif i > 0:
            min_pos = min(min_pos, i) if min_pos else i
    return max_neg, min_pos

